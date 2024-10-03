# data_pipeline/ingestion/ingest_data.py
import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
BASE_URL = "https://www.alphavantage.co/query"


def fetch_stock_data(symbol: str):
    params = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": symbol,
        "apikey": API_KEY,
        "outputsize": "compact",  # Retrieves ~100 days of daily data
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()  # Raise an error for bad status codes
    data = response.json()
    df = pd.DataFrame.from_dict(data["Time Series (Daily)"], orient="index")
    df = df.reset_index().rename(columns={"index": "date"})
    return df


def save_data_to_csv(df, filename):
    df.to_csv(filename, index=False)


if __name__ == "__main__":
    symbol = "AAPL"
    df = fetch_stock_data(symbol)
    save_data_to_csv(df, f"{symbol}_data.csv")
    print(f"Data saved to {symbol}_data.csv")
