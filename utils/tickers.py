import pandas as pd

def get_sp500_tickers():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    df = pd.read_html(url)[0]
    tickers = df["Symbol"].tolist()
    return [ticker.replace(".", "-") for ticker in tickers]  # BRK.B → BRK-B
