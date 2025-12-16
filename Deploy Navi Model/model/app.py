from flask import Flask,request,jsonify
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
from pymongo import MongoClient
from flask_cors import CORS
import jwt
from datetime import datetime
from bson import ObjectId
from dotenv import load_dotenv
import requests
import os
import numpy as np
load_dotenv()

# google api
API_KEY = os.getenv('API_KEY')
CX = os.getenv('CX')

# api fetch
def google_search(query,max_results=6):
   url = "https://www.googleapis.com/customsearch/v1"
   params = {"key": API_KEY, "cx": CX, "q":query}
   response = requests.get(url,params=params)
   data = response.json()


   result = []
   if "items" in data:
      for item in data["items"][:max_results]:
         result.append({
            "title":item.get("title", ""),
            "link":item.get("link", ""),
            "snippet":item.get("snippet", "")

         })
   return result

# model work
df = pd.read_json('dataset.json')
df['question'] = df['question'].apply(lambda x : x.lower())


MONGO_URI = os.getenv('MONGO_URI')
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

client = MongoClient(MONGO_URI)
db = client['roadmapDB']
collection = db['roadmaps']

# model
model  = SentenceTransformer('all-MiniLM-L6-v2')
embeding = model.encode(df['question'].tolist(),convert_to_numpy=True)

threshold = 0.70


app = Flask(__name__)
CORS(app)

@app.route('/roadmap',methods=['POST'])
def chatboat():
    try:
        token = request.headers.get('Authorization',None)
        if not token:
            return jsonify({"Error":"Token is missing"}),401
        
        try:
            token = token.split(" ")[1]
            decoded = jwt.decode(token, JWT_SECRET_KEY,algorithms=["HS256"])

            user_id = decoded.get("userId")
        except Exception:
            return jsonify({"Error":"Token is invalid"}),401
        
        
        data = request.get_json()

        user_input = data.get("question","")

        if not user_input.strip():
            return jsonify({"Error":"question is a required"}),400

        
        # x_user = embedder
        x_user = model.encode([user_input],convert_to_numpy=True)
        similarities = cosine_similarity(x_user, embeding)[0]
        best_index = np.argmax(similarities)


        if similarities[best_index] >= threshold:
           roadmap = df.iloc[best_index]
           output = {
               "predicted_domain":roadmap["question"],
               "roadmap":roadmap["steps"],
           }
        else:
            results  = google_search(user_input)
            output={
                "question":user_input,
                "google_results": results,
                # "roadmap": [],
            }

        send_data={
            "userId":str(user_id),
            "question":user_input,
            "answer":output,
            "type":"bot",
            "timestamp": datetime.utcnow()
               
            }
        
       
        collection.insert_one(send_data)

        return jsonify(output)
        
    except ValueError as e:
        return jsonify({"error": str(e)}), 500


        
@app.route('/getdata',methods=['GET'])
def finddata():

    token = request.headers.get('Authorization', None)
    if not token:
        return jsonify({"Error":"Token is missing"}), 401
    
    try:
            token = token.split(" ")[1]
            decoded = jwt.decode(token, JWT_SECRET_KEY,algorithms=["HS256"])

            user_id = decoded.get("userId")

    except Exception:
            return jsonify({"Error":"Token is invalid"}),401
    
    # getChat = list(collection.find({"userId":user_id},{"_id":0}).sort("timestamp",1))
    getChat = list(collection.find({"userId": user_id}).sort("timestamp", 1))

    for chat in getChat:
        chat["_id"] = str(chat["_id"])
        
    return jsonify(getChat)    


@app.route('/delete/<id>', methods=['DELETE'])
def dataRemove(id):
    try:
        token = request.headers.get('Authorization', None)
        if not token:
            return jsonify({"error": "token not found"}), 404

        token = token.split(" ")[1]
        decoded = jwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'])
        user_id = str(decoded.get("userId"))

        # 🟢 ObjectId banakar delete karo
        result = collection.delete_one({"_id": ObjectId(id), "userId": user_id})

        if result.deleted_count == 0:
            return jsonify({"error": "Message not found"}), 404

        return jsonify({"success": True, "deleted_count": result.deleted_count})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    # app.run(debug=True)
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0",port=port)


