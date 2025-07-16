# Configuration
VERSION = 'V1.2'
SYMBOL = 'BTCUSDT'
SYMBOLS = ['BTC/USDT', 'ETH/USDT', 'SOL/USDT']
SEQ_LEN = 50
SLEEP_TIME = 15
MAX_DAYS=365
API_URL = "https://api.binance.com/api/v3/klines"
TELEGRAM_TOKEN = "7706670085:AAGRMve7EuhFo1i8C2U22JdNPyGyvjN4-N8"
TELEGRAM_CHAT_ID = "7664939619"

TIMEFRAME = '1h'
MODEL_PATH = "crypto_model.keras"

features = [
    'rsi', 'rsi_delta', 'macd', 'macd_signal',
    'ema_20', 'ema_50', 'bb_high', 'bb_low',
    'obv', 'volatility', 'stoch_k', 'stoch_d'
]