import time
from data_fetcher import fetch_klines
from send_telegram_message import notify, buy_notification, sell_notification
from config import SYMBOLS, VERSION, SLEEP_TIME
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

            prediction = predict(model, X)
            if prediction == Prediction.BUY:
                buy_notification(symbol)
            elif prediction == Prediction.SELL:
                sell_notification(symbol)
            else:
                log(f"No action to take.")
        except Exception as e:
            error(f"Exception: {e}")
        finally:
            time.sleep(60)



while True:
    try:
        log("----- Nouvelle exécution -----")
        run()
    except Exception as e:
        error(f"Erreur : {e}")
        
    time.sleep(SLEEP_TIME * 60)