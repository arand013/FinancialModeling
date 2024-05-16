# !pip install pandas
# !pip install yfinance

import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import yfinance as yf
from pandas_datareader import data as pdr

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

#  Annual and Quarterly Financial Statement Summary
ticker.financials

ticker.quarterly_financials

ticker.balance_sheet

ticker.quarterly_balance_sheet

# Annual and Quarterly Cashflow Statement

ticker.cashflow

ticker.quarterly_cashflow

ticker.earnings

ticker.quarterly_earnings


# Sustainability: Environmental, Social and Governance (ESG)

ticker.sustainability



# Analyst Recommendations
ticker.recommendations.info()
ticker.recommendations.tail(10)


# Calendat Upcoming Events
ticker.calendar


#  Option Expiration Dates
ticker.options
expiration = ticker.options[0]
options = ticker.option_chain(expiration)
options.calls.info()
options.calls.head()
options.puts.info()


# Data Download with A Proxy Server
PROXY_SERVER = 'PROXY_SERVER'


ticker.trend_details
ticker.quarterly_income_stmt
ticker.quarterly_balance_sheet

ticker._download_options
ticker._download_options('2023-012-15', '2024-05-15')


# Downloading Multiple Symbols

tickers = yf.Tickers('msft aapl goog')
print(tickers)
print(tickers.info())

print(pd.Series(tickers.tickers['MSFT'].info))

print(tickers.tickers['AAPL'].history(period="1mo"))

print(tickers.history(period='1mo').stack(-1))

data = yf.download("SPY AAPL", start="2023-12-01", end="2024-05-15")

data.info()

data = yf.download(
        tickers = "SPY AAPL MSFT", # list or string

        # use "period" instead of start/end
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # (optional, default is '1mo')
        period = "5d",

        # fetch data by interval (including intraday if period < 60 days)
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        # (optional, default is '1d')
        interval = "1m",

        # group by ticker (to access via data['SPY'])
        # (optional, default is 'column')
        group_by = 'ticker',

        # adjust all OHLC automatically
        # (optional, default is False)
        auto_adjust = True,

        # download pre/post regular market hours data
        # (optional, default is False)
        prepost = True,

        # use threads for mass downloading? (True/False/Integer)
        # (optional, default is True)
        threads = True,

        # proxy URL scheme use use when downloading?
        # (optional, default is None)
        proxy = None
    )

data.info()

yf.pdr_override()

# download dataframe
data = pdr.get_data_yahoo('SPY',
                          start='2017-01-01',
                          end='2019-04-30',
                          auto_adjust=False)

# auto_adjust = True
data.tail()

# auto_adjust = False
data.tail()