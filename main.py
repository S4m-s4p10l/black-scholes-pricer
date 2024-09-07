import numpy as np
import streamlit as lt
from scipy.stats import norm


N = norm.cdf

'''
S - price of the underlying asset
K - strike price
r - interest rate
v - standard deviation of returns(volatility)
t - time to expiration
'''


def brm(S, K, r, v, t, type="CALL"):
    d1 = (np.log(S/K)+(r+v**2/2)*t)/(v*np.sqrt(t))
    d2 = d1 - v*np.sqrt(t)
    res = S*N(d1)-K*np.exp(-r*t)*N(d2)
    if type == "CALL":
        return res
    elif type == "PUT":
        return -1*res
    
    
print(brm(100, 120, 0.1, 0.2, 1))
    
