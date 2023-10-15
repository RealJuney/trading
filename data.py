import yfinance as yf
import pandas as pd


tickers = ['AAPL', 'GOOGL']

train_start_date = "2023-10-09"
train_end_date = "2023-10-13"


df = None

for ticker in tickers:

    data = yf.download(tickers=ticker,
                    start=train_start_date,
                    end=train_end_date,
                    interval="1m"
                    )

    data.reset_index(inplace=True)
    data.insert(0, 'tic', [ticker] * data.shape[0])
    data.columns = data.columns.str.lower()
    
    if df is None:
        df = data
    else:
        df.append(data)

print(df)