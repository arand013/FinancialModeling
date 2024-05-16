# !pip install pandas
# !pip install yfinance

import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import yfinance as yf

symbol = 'T'
ticker = yf.Ticker(symbol)
pd.Series(ticker.info).head(20)

data = ticker.history(period='5d',
                      interval='1m',
                      start=None,
                      end=None,
                      actions=True,
                      auto_adjust=True,
                      back_adjust=False)
data.info()

# show actions (dividends, splits)
ticker.actions

ticker.dividends

ticker.splits
