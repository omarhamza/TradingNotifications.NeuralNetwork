import ccxt
import pandas as pd
import time
from config import TIMEFRAME, MAX_DAYS


def fetch_klines(symbol):
    exchange = ccxt.binance()
    since = exchange.parse8601((pd.Timestamp.utcnow() - pd.Timedelta(days=MAX_DAYS)).isoformat())

    all_candles = []
    while True:
        candles = exchange.fetch_ohlcv(symbol, timeframe=TIMEFRAME, since=since, limit=500)
        if not candles:
            break
        all_candles.extend(candles)
        since = candles[-1][0] + 1  # next timestamp (avoid duplicates)
        time.sleep(exchange.rateLimit / 1000)  # respect rate limit

    df = pd.DataFrame(all_candles, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)

    df = df[~df.index.duplicated(keep='last')]
    df.sort_index(inplace=True)

    return df
