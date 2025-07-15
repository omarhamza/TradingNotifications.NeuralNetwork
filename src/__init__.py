# train_model.py

import time
from data_fetcher import fetch_klines
# from model import predict_next
from utils import log, normalize_array
from config import SEQ_LEN, MODEL_PATH
import numpy as np
import tensorflow as tf
from send_telegram_message import notify

notify(f"✅ *Start running NN V1.0!*")

# === Fonction pour transformer les données en séquences ===
def create_sequences(data, seq_len):
    X, y = [], []
    for i in range(len(data) - seq_len):
        X.append(data[i:i + seq_len])
        y.append(data[i + seq_len])
    return np.array(X), np.array(y)

# === Pipeline d'entraînement ===
def train_model():
    print("📥 Téléchargement des données depuis Binance...")
    df = fetch_klines()

    prices = df["close"].values
    norm_prices, _, _ = normalize_array(prices)

    X, y = create_sequences(norm_prices, SEQ_LEN)
    X = X.reshape((X.shape[0], X.shape[1], 1))

    print(f"🧠 Entraînement du modèle sur {X.shape[0]} exemples...")

    model = tf.keras.Sequential([
        tf.keras.layers.LSTM(64, input_shape=(SEQ_LEN, 1)),
        tf.keras.layers.Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y, epochs=10, batch_size=32)

    model.save(MODEL_PATH)
    print(f"✅ Modèle enregistré dans : {MODEL_PATH}")

    prediction = model.predict(X)
    shouldIBuyCrypto = float(prediction[0][0])
    log(f"prediction-----------: {shouldIBuyCrypto:.2f}")

    log("keras--------------------")
    print(model.summary())

    if prediction[0][0] >= 0.5:
        notify(f"Buy BTC \n score: {shouldIBuyCrypto:.2f}")

    # if len(prices) >= 50:
    #     prediction = predict_next(prices)
    #     log(f"Prix actuel: {df['close'].iloc[-1]:.2f}, Prédiction: {prediction:.2f}")
    # else:
    #     log("Pas assez de données pour faire une prédiction.")


if __name__ == "__main__":
    while True:
        try:
            print("----- Nouvelle exécution -----")
            train_model()
        except Exception as e:
            print(f"Erreur : {e}")
            
        time.sleep(15 * 60)  # 15 minutes