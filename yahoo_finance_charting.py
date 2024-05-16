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

# Overview of closing price before calculating DMAs
sns.set_style('darkgrid')
plt.figure(figsize = (7,5), dpi = 100)
plt.title('Closing Price')
plt.plot(df['Close']) 

# Calculate 50DMA
df['fiftyDMA'] = df['Close'].rolling(50).mean()

# Calculate 200DMA
df['thDMA'] = df['Close'].rolling(200).mean()

df.describe()
