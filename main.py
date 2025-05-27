import time
from utils.tickers import get_sp500_tickers
from data_loader.fetcher import fetch_ohlcv
from data_loader.db_writer import get_engine, write_to_db
import pandas as pd

# Таймфрейми і періоди
timeframes = {
    "1d": "2y",
    "1h": "20d",
    "5m": "2d"
}

def process_all():
    tickers = get_sp500_tickers()
    engine = get_engine()

    for interval, period in timeframes.items():
        print(f"\n=== Завантаження для {interval} ({period}) ===")
        start = time.perf_counter()
        all_data = []

        for ticker in tickers:
            df = fetch_ohlcv(ticker, interval, period)
            if df is not None:
                all_data.append(df)

        if all_data:
            combined_df = pd.concat(all_data, ignore_index=True)
            write_to_db(combined_df, engine)

        end = time.perf_counter()
        print(f">>> Завантажено і збережено за {end - start:.2f} секунд ({interval})")

if __name__ == "__main__":
    process_all()
