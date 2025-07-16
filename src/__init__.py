import time
from data_fetcher import fetch_klines
from send_telegram_message import notify, buy_notification
from config import SYMBOL, VERSION
from indicators import add_indicators
from train_model import train_model
from predict import predict
from utils import log, error, save_to_csv

notify(f"✅ *Start running NN {VERSION}!*")

# === Pipeline d'entraînement ===
def run():
    print("📥 Téléchargement des données depuis Binance...")
    df = fetch_klines()
    df = add_indicators(df)
    
    save_to_csv(df, SYMBOL)
    
    model, X = train_model(df)

    if predict(model, X):
        buy_notification()


while True:
    try:
        log("----- Nouvelle exécution -----")
        run()
    except Exception as e:
        error(f"Erreur : {e}")
        
    time.sleep(15 * 60)  # 15 minutes