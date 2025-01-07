# American-Option-Pricing-Condition-With-Stopping-Process

This project implements an American-style option pricer using the binomial tree method, based on Chapter 4 of **"Stochastic Calculus for Finance I"** by Steven E. Shreve. The pricer supports both call and put options and accounts for early exercise, making it ideal for valuing American options.

## Overview

The American Binomial Option Pricer calculates the value of American options by simulating the asset price evolution and incorporating the flexibility of early exercise. It outputs several intermediate results, such as asset price trees and discounted payoffs, for better understanding and visualization.

## Features

- **Supports Both Call and Put Options:** The model can price both types of American options.
- **Customizable Inputs:** Users can specify stock price, strike price, time to maturity, volatility, and more.
- **Detailed Outputs:** Provides:
  - Asset price tree
  - Option price tree
  - Stopped process tree for early exercise
  - Discounted payoff tree
- **Risk-Neutral Valuation Framework:** Ensures accuracy in pricing.

## How It Works

1. **Binomial Tree Construction:** Simulates potential future stock prices using up and down factors.
2. **Backward Induction:** Calculates option prices from the terminal nodes backward to the initial node.
3. **Early Exercise Check:** Compares intrinsic value and discounted continuation value at each node to decide whether early exercise is optimal.
4. **Stopped Process Propagation:** Tracks and propagates the early exercise value throughout the tree.

## Parameters

| Parameter  | Description                                                                 |
|------------|-----------------------------------------------------------------------------|
| `S`        | Initial stock price                                                        |
| `K`        | Strike price                                                               |
| `T`        | Time to maturity (in years)                                                |
| `N`        | Number of steps in the binomial tree                                       |
| `r`        | Risk-free interest rate (annualized)                                       |
| `sigma`    | Volatility of the underlying asset (annualized)                            |
| `put_call` | Type of option: `'call'` for call options, `'put'` for put options         |

## Outputs

The pricer generates the following:

- **Asset Prices Tree:** A matrix representing simulated stock prices at each node.
- **Option Prices Tree:** The computed option values at every step.
- **Stopped Process Tree:** Tracks where early exercise occurs and propagates the value forward.
- **Discounted Payoff Tree:** Computes the present value of payoffs at each node.

## Advanced Concepts

- **Up-Factor (`u`)**: Represents the upward movement of stock prices and is calculated as `u = exp(sigma * sqrt(dt))`.
- **Down-Factor (`d`)**: Represents the downward movement of stock prices, calculated as `d = exp(-sigma * sqrt(dt))`.
- **Risk-Neutral Probability (`p`)**: The probability of an upward move in the risk-neutral world, `p = (exp(-r * dt) - d) / (u - d)`.

These calculations ensure consistency with the no-arbitrage principle and provide accurate valuation for American options.

## Example Usage

```python
S = 50       # Initial stock price
K = 49       # Strike price
T = 1        # Time to maturity
N = 3        # Number of steps
r = 0.05     # Risk-free rate
sigma = 0.2  # Volatility
put_call = 'call'

asset_prices, option_prices, stopped_process, discounted_payoff = american_binomial_pricer(S, K, T, N, r, sigma, put_call)

print("Asset Prices:")
print(asset_prices)
print("\nOption Prices:")
print(option_prices)
print("\nStopped Process:")
print(stopped_process)
print("\nDiscounted Payoff:")
print(discounted_payoff)
