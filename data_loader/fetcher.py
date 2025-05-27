import yfinance as yf

def fetch_ohlcv(ticker, interval, period):
    try:
        df = yf.download(ticker, interval=interval, period=period, progress=False)
        if df.empty:
            return None
        df = df.reset_index()
        df["ticker"] = ticker
        df["interval"] = interval
        df = df.rename(columns={
            "Date": "datetime",
            "Open": "open",
            "High": "high",
            "Low": "low",
            "Close": "close",
            "Volume": "volume"
        })
        return df[["ticker", "datetime", "open", "high", "low", "close", "volume", "interval"]]
    except Exception as e:
        print(f"Error fetching {ticker} ({interval}): {e}")
        return None
