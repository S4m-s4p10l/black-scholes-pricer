import numpy as np
import streamlit as st
from scipy.stats import norm
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

N = norm.cdf


#S - price of the underlying asset
#K - strike price
#r - interest rate
#v - standard deviation of returns(volatility)
#t - time to expiration



def brm(S, K, r, v, t, type="CALL"):
    d1 = (np.log(S/K)+(r+v**2/2)*t)/(v*np.sqrt(t))
    d2 = d1 - v*np.sqrt(t)
    res = S*N(d1)-K*np.exp(-r*t)*N(d2)
    if type == "CALL":
        return res
    elif type == "PUT":
        return -1*res
    
st.title("Black-Scholes model")

min_strike = st.sidebar.number_input("Min strike price", 1)
max_strike = st.sidebar.number_input("Max strike price", 2)
asset = st.sidebar.number_input("Price of the underlying asset", 50)
rate = st.sidebar.number_input("Interest rate", 2)
volatility = st.sidebar.number_input("Standard deviation of annualised return (volatility)", 5)
min_time = st.sidebar.number_input("Min time to expiration", 1)
max_time = st.sidebar.number_input("Max time to expiration", 2)

strike_list = np.linspace(min_strike, max_strike, num=10)
time_list = np.linspace(min_time, max_time, num=10)


data = []
for i in strike_list:
    for j in time_list:
        row = [i, j, brm(asset, i, rate, volatility, j)]
        data.append(row)

        
df = pd.DataFrame(data)
fig, ax = plt.subplots()
sns.heatmap(df.corr(), ax=ax)
st.write(fig)