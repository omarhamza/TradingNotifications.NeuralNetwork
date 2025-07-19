import time
from data_fetcher import fetch_klines
from send_telegram_message import notify, buy_notification, sell_notification
from config import SYMBOLS, VERSION
from indicators import add_indicators
from entities.Prediction import Prediction
from train_model import train_model
from predict import predict
from utils import log, error, save_to_csv

notify(f"✅ *Start running NN {VERSION}!*")

# === Pipeline d'entraînement ===
def run():
    for symbol in SYMBOLS:
        try:
            log(f"📥 Téléchargement des données {symbol} depuis Binance...")
            df = fetch_klines(symbol)
            df = add_indicators(df)
            
            save_to_csv(df, symbol)
            
            model, X = train_model(df)

            prediction, score = predict(model, X)
            if prediction == Prediction.BUY:
                buy_notification(symbol, score)
            elif prediction == Prediction.SELL:
                sell_notification(symbol, score)
            else:
                log(f"No action to take.")
        except Exception as e:
            notify(f"❌❌❌ Erreur globale : {e}")
        finally:
            time.sleep(5)

try:
    log("----- Nouvelle exécution -----")
    run()
except Exception as e:
    notify(f"❌❌❌ Erreur globale : {e}")