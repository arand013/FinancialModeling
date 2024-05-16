
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import yfinance as yf
symbol = 'FB'
ticker = yf.Ticker(symbol)
pd.Series(ticker.info).head(20)
