import numpy as np
from joblib import load
from flask_cors import CORS
from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model

app = Flask(__name__)

CORS(app,resources={r"/*":{"origins":"*"}})

model = load_model('model/Option_Pricing_Model.keras')

scaler = load('model/scaler.joblib')


@app.route('/', methods=['GET'])
def get_data():
    data = {
        "message":"API is Running"
    }
    return jsonify(data)

@app.route('/predict', methods=['POST'])
def predict():

    data = request.get_json()
    stock_price = data['stockPrice']
    strike_price = data['strikePrice']
    time_to_expiration = data['timeToExpiration']
    risk_free_rate = data['riskFreeRate']
    volatility = data['volatility']

    input_data = np.array([[stock_price, strike_price, time_to_expiration, risk_free_rate, volatility]])

    input_data = scaler.transform(input_data)

    prediction = model.predict(input_data)

    predicted_value = float(prediction[0][0])

    return jsonify({"predicted_value": predicted_value})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

""" set FLASK_APP=flaskServer.py
$env:FLASK_APP = "flaskServer.py"
flask run """