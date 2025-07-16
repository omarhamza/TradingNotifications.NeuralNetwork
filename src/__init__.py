import time
from data_fetcher import fetch_klines
from send_telegram_message import notify, buy_notification
from train_model import train_model
from predict import predict
from utils import log, error

notify(f"✅ *Start running NN V1.1!*")

# === Pipeline d'entraînement ===
def run():
    print("📥 Téléchargement des données depuis Binance...")
    df = fetch_klines()

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