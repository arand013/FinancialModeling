import numpy as np
import pandas as pd

from statsmodels.tsa.stattools import coint, adfuller
from statsmodels.tools.tools import add_constant
from statsmodels.regression.linear_model import OLS

import yfinance as yf

import matplotlib.pyplot as plt

Tickers = ['JPM', 'BAC', 'WFC', 'C', 'BLK', 'GS', 'MS', 'SCHW', 'AXP', 'USB', 'TFC', 'PNC', 'BK', 'COF', 'STT', 'FITB']

data = yf.download(Tickers, start="2018-01-01", end="2023-01-01")
df = data["Adj Close"].dropna(how="all")

df.tail()