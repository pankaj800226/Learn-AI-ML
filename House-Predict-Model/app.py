from flask import Flask, request, jsonify
import pickle
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


with open('house_model.pkl','rb') as f:
    rfr = pickle.load(f)

with open('city_model.pkl','rb') as f:
    encoded_city_val = pickle.load(f)

with open('location_model.pkl','rb') as f:
    location_encoder_val = pickle.load(f)


@app.route('/predict',methods=['POST'])
def predic():
    data = request.json

    try:
      data = {k.lower(): v for k, v in request.json.items()}
      area_sqft  = int(data['area_sqft'])
      bedroom    = int(data['bedrooms'])
      bathroom   = int(data['bathrooms'])
      city       = data['city']
      location   = data['location']


      encoded_city = encoded_city_val.transform([city])[0]
      encode_loaction = location_encoder_val.transform([location])[0]

    # feature 
      new_house = [[area_sqft,bedroom,bathroom,encoded_city,encode_loaction]]
      predect_price = rfr.predict(new_house)[0]

      return jsonify({
            "Area_sqft": area_sqft,
            "Bedroom": bedroom,
            "Bathroom": bathroom,
            "City": city,
            "Location": location,
            "Predicted_Price": f"{predect_price:.2f} INR"
        })



    except ValueError as e:
      return jsonify({"error":f"{e} Please enter valid city and location from dataset"}),400


# -----------------------------
if __name__ == '__main__':
    app.run(debug=True)
