# Option Pricing with Neural Networks

This repository implements a neural network-based approach for pricing financial options and computing implied volatilities. The solution accelerates the computation process by training Artificial Neural Networks (ANNs) on data generated from financial models like Black-Scholes and Heston stochastic volatility.

## Features

- **Fast Option Pricing:** Leverages ANNs to speed up the calculation of option prices.
- **Implied Volatility Computation:** Efficiently computes implied volatilities using a trained neural network.
- **Supports Multiple Models:** Compatible with Black-Scholes and Heston stochastic volatility models.
- **GPU Acceleration:** Optimized for running on GPUs, significantly reducing computation time.

## Installation

To use this project, clone the repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/option-pricing-nn.git
cd option-pricing-nn
pip install -r requirements.txt
