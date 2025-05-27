import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def get_engine():
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    db = os.getenv("DB_NAME")
    return create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

def write_to_db(df, engine):
    try:
        df.to_sql("stock_prices", engine, if_exists="append", index=False, method="multi")
    except Exception as e:
        print(f"Error writing to DB: {e}")
