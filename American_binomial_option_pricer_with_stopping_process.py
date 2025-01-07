#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 14:31:26 2025

@author: Tayyib Salawu
"""
import numpy as np
import pandas as pd

def american_binomial_pricer(S, K, T, N, r, sigma, put_call):
    
    dt = T / N
    u = np.exp(sigma * np.sqrt(dt))
    d = np.exp(-sigma * np.sqrt(dt))
    p = (np.exp(-r * dt) - d) / (u - d)
    q = 1- p
    
    asset_prices = pd.DataFrame(np.zeros((N+1, N+1)))
    asset_prices.iloc[0, 0] = S
    
    for j in range(1, N+1):
        for i in range(j+1):
            if i == 0:
                asset_prices.iloc[i, j] = asset_prices.iloc[i, j-1] * u
            else:
                asset_prices.iloc[i, j] = asset_prices.iloc[i-1, j-1] * d
                
    option_prices = pd.DataFrame(np.zeros((N+1, N+1)))            
    for i in range(N+1):
        if put_call == 'call':
            option_prices.iloc[i, N] = max(asset_prices.iloc[i, N] - K, 0)
        if put_call == 'put':
            option_prices.iloc[i, N] = max(K - asset_prices.iloc[i, N], 0)
    
    for j in range(N-1, -1, -1):
        for i in range(j+1):
            if put_call == 'call': 
                option_prices.iloc[i, j] = max(np.exp(-r * dt) * ((p * option_prices.iloc[i, j+1]) + (q * option_prices.iloc[i+1, j+1])), asset_prices.iloc[i, j] - K)
            if put_call == 'put':
                option_prices.iloc[i, j] = max(np.exp(-r * dt) * ((p * option_prices.iloc[i, j+1]) + (q * option_prices.iloc[i+1, j+1])), K - asset_prices.iloc[i, j])
              
                 
    stopped_process = pd.DataFrame(np.zeros((N+1, N+1)))
    
    for j in range(N+1):
        for i in range(j+1):
            stopped_process.iloc[i, j] = option_prices.iloc[i, j] * np.exp(-r * dt * j)
            
    discounted_payoff = pd.DataFrame(np.zeros((N+1, N+1)))
    
    for j in range(N+1):
        for i in range(j+1):
            if put_call == 'call':
                discounted_payoff.iloc[i, j] = max(asset_prices.iloc[i, j] - K, 0) * np.exp(-r * dt * j)
            if put_call == 'put':
                discounted_payoff.iloc[i, j] = max(K - asset_prices.iloc[i, j], 0) * np.exp(-r * dt * j)
            
    for j in range(N):  # Forward iteration over time steps
        for i in range(j+1):
            if stopped_process.iloc[i, j] == discounted_payoff.iloc[i, j]:
                stopped_process.iloc[i, j+1:] = stopped_process.iloc[i, j]
                stopped_process.iloc[i+1, j+1:] = stopped_process.iloc[i, j]
            
        
            
            
    return asset_prices, option_prices, stopped_process, discounted_payoff




# Assuming your american_binomial_pricer function is defined above
# Test the function with the example parameters
S = 50       # Initial stock price
K = 49      # Strike price
T = 1        # Time to maturity
N = 3        # Number of steps
r = 0.05     # Risk-free rate
sigma = 0.2  # Volatility
put_call = 'call'

# Call the function
asset_prices, option_prices, stopped_process, discounted_payoff = american_binomial_pricer(S, K, T, N, r, sigma, put_call)

# Print results
print("Asset Prices:")
print(asset_prices)
print("\nOption Prices:")
print(option_prices)
print("\nStopped Process:")
print(stopped_process)
print("\nDiscounted Payoff:")
print(discounted_payoff)



    
            
        
   