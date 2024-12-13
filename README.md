# Option Pricing and Implied Volatility using Neural Networks

This project uses TensorFlow-based Artificial Neural Networks (ANNs) to price financial options and compute implied volatilities, accelerating traditional numerical methods. The ANN is trained using financial models like Black-Scholes and Heston, offering substantial computational speed improvements without sacrificing accuracy. It also features a Flask backend with a ReactJS frontend for an interactive interface.

## Requirements
- Python 3.x
- TensorFlow
- pandas
- Flask
- ReactJS
- NumPy

## Installation

1. Clone the repository:
    ```bash
    git clone (https://github.com/JalendraIITP/Option_Pricing_using_Machine_Learning.git)
    cd Option_Pricing_using_Machine_Learning
    ```

2. Install the Python dependencies:
   Start the virtual environment and Install all packages
    ```bash
    pip install -r requirements.txt
    ```

4. Navigate to the `frontend` folder and install the ReactJS dependencies:
    ```bash
    npm install
    ```

5. Run the Flask backend:
    ```bash
    python flaskServer.py
    ```

6. Run the ReactJS frontend:
    ```bash
    npm start
    ```
![Frontend View of the Project](https://github.com/JalendraIITP/Option_Pricing_using_Machine_Learning/blob/master/Option_Pricing.png)
