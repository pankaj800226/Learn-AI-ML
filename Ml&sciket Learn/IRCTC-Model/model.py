from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import re
import pickle


app = Flask(__name__)
CORS(app)

# Load dataset
df = pd.read_json("pk.json")

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

keywords_list = ['banaya', 'make', 'made', 'develop', 'create', 'you']

def keywords_detect(user_input: str):
    user_input_words = re.sub(r'[^\w\s]', '', user_input.lower()).split()
    if any(word in user_input_words for word in keywords_list):
        return 'ask_creator'
    return 'train_price'


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    user_input = data.get("question", "").lower()

    # Detect intent
    intent = keywords_detect(user_input)

    if intent == 'ask_creator':
        # return jsonify({"response": "I am RailAi Model created by Pankaj Singh"})
           return jsonify({
            "intent": "ask_creator",
            "message": "I am RailAi Model created by Pankaj Singh 😎"
        })

    elif intent == 'train_price':
        train_data = df[df['TrainName'].str.lower().str.contains(user_input)]
        if train_data is not None and not train_data.empty:
            avg_seats = train_data['SeatsAvailable'].mean()

            base_price = train_data['BasePrice'].iloc[0]

            predicted_price = model.predict([[avg_seats, base_price]])[0]

            explanation = train_data['Explanation'].iloc[0]
            
            return jsonify({
                "intent": "train_price",
                "train": user_input,
                "predicted_price": round(predicted_price, 2),
                "explanation": explanation
            })
        else:
            return jsonify({"error": "Train not found"})
    else:
        return jsonify({"error": "Unknown intent"})


if __name__ == "__main__":
    app.run(debug=True)
