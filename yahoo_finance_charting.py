# First PIP install all packages
#  !pip install yfinance

# import Libraries
import warnings
warnings.filterwarnings('ignore')

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import library for Statsmodels Formula(SMF)
import statsmodels.formula.api as smf

ticker = "AAPL"
start_date = "2020-05-14"
end_date = "2024-05-14"

df = yf.download(ticker, start=start_date, end=end_date)

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

# Plot Closing Price vs 50DMA vs 200DMA
sns.set_style('darkgrid')
plt.figure(figsize = (7,5), dpi = 100)
plt.title('Closing Price vs 50DMA vs 200DMA')
plt.plot(df['Close'], label = 'Close')
plt.plot(df['fiftyDMA'], label = '50DMA')
plt.plot(df['thDMA'], label = '200DMA')
plt.legend()


# Probabilistic Futurisitive Movement of the Stock 
# Analyzing correlation between each variables
plt.figure(figsize=(7,7), dpi=100)
sns.heatmap(df.corr(), annot=True)


# Plot Distplot of 50DMA
sns.set_style('darkgrid')
plt.figure(figsize = (7,5), dpi = 100)
plt.title('Distplot of 50DMA')
sns.distplot(df['fiftyDMA'])


# Plot Distplot of the close price
sns.set_style('darkgrid')
plt.figure(figsize = (7,5), dpi = 100)
plt.title('Distplot of the close price')
sns.distplot(df['Close'])

model = smf.ols(formula = 'Close~fiftyDMA', data = df)
model = model.fit()

model.summary()


sns.set_style('darkgrid')
plt.figure(figsize = (7,5), dpi = 100)
plt.title('Closing Price vs 50DMA vs 200DMA')
plt.plot(df['Close'], label = 'Close')
plt.plot(df['fiftyDMA'], label = '50DMA')
plt.plot(df['thDMA'], label = '200DMA')
plt.legend()