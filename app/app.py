import streamlit as st
import pandas as pd
# import yfinance as yf
import joblib

from ta.momentum import RSIIndicator
from ta.trend import MACD

# Load model
model = joblib.load("../models/random_forest.pkl")

st.title("Crypto Price Prediction Dashboard")

st.write("AI-powered Bitcoin trend prediction")

btc = pd.read_csv(
    "../data/BTC-USD.csv",
    sep=";"
)
# print(btc.columns)
btc["timestamp"] = pd.to_datetime(
    btc["timestamp"]
)

btc.set_index("timestamp", inplace=True)

btc.columns = btc.columns.get_level_values(0)

# Features
btc["MA7"] = btc["close"].rolling(7).mean()

btc["MA30"] = btc["close"].rolling(30).mean()

btc["Daily_Return"] = btc["close"].pct_change()

btc["Volatility"] = (
    btc["Daily_Return"]
    .rolling(7)
    .std()
)

# RSI
rsi = RSIIndicator(close=btc["close"])

btc["RSI"] = rsi.rsi()

# MACD
macd = MACD(close=btc["close"])

btc["MACD"] = macd.macd()

btc = btc.dropna()

# Latest row
latest = btc.iloc[-1]

features = [[
    latest["open"],
    latest["high"],
    latest["low"],
    latest["close"],
    latest["volume"],
    latest["MA7"],
    latest["MA30"],
    latest["Daily_Return"],
    latest["Volatility"],
    latest["RSI"],
    latest["MACD"]
]]

# Prediction
prediction = model.predict(features)[0]

# Display prediction
st.subheader("AI Prediction")

if prediction == 1:
    st.success("Bitcoin price may go UP tomorrow ")
else:
    st.error("Bitcoin price may go DOWN tomorrow")

# BTC chart
st.subheader("Bitcoin Closing Price")

st.line_chart(btc["close"])

# Show latest data
st.subheader("Latest Market Data")

st.dataframe(btc.tail())