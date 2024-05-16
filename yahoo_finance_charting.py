# First PIP install all packages
#  !pip install yfinance

# import Libraries
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
# Import library for Statsmodels Formula(SMF)
import statsmodels.formula.api as smf

ticker = "AAPL"
start_date = "2020-05-14"
end_date = "2024-05-14"

df = yf.download(ticker, start=start_date, end=end_date)

warnings.filterwarnings('ignore')
%matplotlib inline

df.head()

df.tail()

df.shape

df.describe()
