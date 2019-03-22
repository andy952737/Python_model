import requests
import pandas as pd

site = "https://query1.finance.yahoo.com/v7/finance/download/2330.TW?period1=0&period2=1549258857&interval=1d&events=history&crumb=hP2rOschxO0"
response = requests.post(site)
# print(response.text) 

with open('data/stock.csv', 'w') as f:
 f.writelines(response.text)
  
#before
# df = pd.read_csv('data/stock.csv')
# print(df.head())

#after
df = pd.read_csv('data/stock.csv', index_col='Date', parse_dates=['Date'])
print(df.head())

df.Close.plot()