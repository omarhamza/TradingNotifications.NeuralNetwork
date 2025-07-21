# Configuration
VERSION = 'V1.4.1'
SYMBOLS = ['BTC/USDT', 'ETH/USDT', 'SOL/USDT', 'XRP/USDT']
SEQ_LEN = 60
MAX_DAYS=365
API_URL = "https://api.binance.com/api/v3/klines"
TELEGRAM_TOKEN = ""
TELEGRAM_CHAT_ID = ""

TIMEFRAME = '1h'
MODEL_PATH = "crypto_model.keras"
SCALER_X_PATH = "scaler_X.pkl"
SCALER_Y_PATH = "scaler_Y.pkl"

LIMIT = 1000
PRED_HOURS = 24
SCALER_PATH = "eth_scaler.pkl"

features = [
    'close',
    'rsi', 'rsi_delta',
    'macd', 'macd_signal', 'ema_20', 'ema_50', 
    'bb_high', 'bb_low',
    'obv', 'volatility', 
    'stoch_k', 'stoch_d'
]