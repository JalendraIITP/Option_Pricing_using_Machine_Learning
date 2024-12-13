import os
import torch
import numpy as np
from joblib import load
from flask_cors import CORS
from scipy.stats import norm
from Ann import ANN_BlackScholes
from flask import Flask, request, jsonify

# Flask app initialization
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

model = None
scaler = None

try:
    model = ANN_BlackScholes(input_size=4, num_classes=1)
    model.load_state_dict(torch.load('model/Option_Pricing_Model.pth', map_location=torch.device('cpu'), weights_only=True))
    model.eval()

    # Load the scaler
    scaler = load('model/scaler.joblib')

    print("Model and scaler loaded successfully.")

except Exception as e:
    print(f"Failed to load model or scaler: {e}")
    exit(1)

@app.route('/', methods=['GET'])
def get_data():
    data = {
        "message": "API is Running"
    }
    return jsonify(data)

def Black_Scholes(money_ness, T, r, sigma):
  d1 = (np.log(money_ness) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
  d2 = d1 - sigma * np.sqrt(T)
  Call_Prices = money_ness * norm.cdf(d1) - np.exp(-r * T) * norm.cdf(d2)
  return Call_Prices

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse JSON input
        data = request.get_json()
        stock_price = data['stockPrice']
        strike_price = data['strikePrice']
        time_to_expiration = data['timeToExpiration']
        risk_free_rate = data['riskFreeRate']
        volatility = data['volatility']

        expected_value = strike_price * Black_Scholes(stock_price / strike_price, time_to_expiration, risk_free_rate, volatility)
        # Prepare input data for the model
        input_data = np.array([[stock_price / strike_price, time_to_expiration, risk_free_rate, volatility]])

        # Convert to torch tensor
        input_tensor = torch.tensor(input_data, dtype=torch.float32)
        
        # Make prediction
        with torch.no_grad():
            prediction = model(input_tensor)

        predicted_value_normalized = float(prediction.item())
        predicted_value = scaler.inverse_transform([[predicted_value_normalized]])[0, 0]

        return jsonify({"predicted_value": round(strike_price * predicted_value, 3),"Actual_Value": round(expected_value, 3)})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
