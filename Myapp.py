import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of google!

""")

# Define the ticker symbol
tickerSymbol = 'GOOGL'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for the ticker
tickerDF = tickerData.history(period='1d', start='2010-5-31', end='2023-5-31')

# Open Charts
st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)

