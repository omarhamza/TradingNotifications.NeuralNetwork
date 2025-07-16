from utils import  normalize_array
from config import SEQ_LEN, MODEL_PATH
import numpy as np
import tensorflow as tf

# === Fonction pour transformer les données en séquences ===
def create_sequences(data, seq_len):
    X, y = [], []
    for i in range(len(data) - seq_len):
        X.append(data[i:i + seq_len])
        y.append(data[i + seq_len])
    return np.array(X), np.array(y)

# === Pipeline d'entraînement ===
def train_model(df):
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

    return model, X