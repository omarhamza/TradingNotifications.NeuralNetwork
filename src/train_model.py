from utils import  normalize_array
from config import SEQ_LEN, MODEL_PATH, features
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
    columns = df[features].values
    norm_features, _, _ = normalize_array(columns)

    X, y = create_sequences(norm_features, SEQ_LEN)
    X = X.reshape((X.shape[0], X.shape[1], X.shape[2]))

    print(f"🧠 Entraînement du modèle sur {X.shape[0]} exemples...")

    model = tf.keras.Sequential([
        tf.keras.layers.LSTM(64, input_shape=(SEQ_LEN, X.shape[2])),
        tf.keras.layers.Dense(1)
    ])

    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y, epochs=10, batch_size=32)

    model.save(MODEL_PATH)
    print(f"✅ Modèle enregistré dans : {MODEL_PATH}")

    return model, X
