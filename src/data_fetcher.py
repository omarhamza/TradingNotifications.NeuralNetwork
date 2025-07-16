import requests
import pandas as pd
from config import API_URL, SYMBOL, TIMEFRAME, MAX_DAYS
from utils import save_to_csv

def fetch_klines(limit=1000):
    url = f"{API_URL}?symbol={SYMBOL}&interval={INTERVAL}&limit={limit}"
    response = requests.get(url)
    data = response.json()
    
    df = pd.DataFrame(data, columns=[
        "timestamp", "open", "high", "low", "close", "volume",
        "close_time", "quote_asset_volume", "num_trades",
        "taker_buy_base", "taker_buy_quote", "ignore"
    ])
    df["close"] = df["close"].astype(float)

    # ---- Save data frame to csv file    
    save_to_csv(df, SYMBOL)

    return df
