import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
import joblib
from config import SEQ_LEN, MODEL_PATH, SCALER_X_PATH, SCALER_Y_PATH, features

def create_sequences(data, seq_len):
    X, y = [], []
    for i in range(len(data) - seq_len):
        X.append(data[i:i + seq_len])
        y.append(data[i + seq_len][0])  # Prédit 1re feature (ex: close)
    return np.array(X), np.array(y)

# === Entraînement modèle ===
def train_model(df):
    raw_features = df[features].values

    scaler_X = MinMaxScaler()
    features_scaled = scaler_X.fit_transform(raw_features)

    X_seq, y_seq = create_sequences(features_scaled, SEQ_LEN)

    scaler_y = MinMaxScaler()
    y_scaled = scaler_y.fit_transform(y_seq.reshape(-1, 1)).flatten()

    X_seq = X_seq.reshape((X_seq.shape[0], X_seq.shape[1], X_seq.shape[2]))


    print(f"🧠 Entraînement du modèle sur {X_seq.shape[0]} exemples...")
    
    model = tf.keras.Sequential([
        tf.keras.layers.LSTM(64, input_shape=(SEQ_LEN, X_seq.shape[2])),
        tf.keras.layers.Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')

    model.fit(X_seq, y_scaled, epochs=10, batch_size=32)

    # Sauvegardes
    model.save(MODEL_PATH)
    joblib.dump(scaler_X, SCALER_X_PATH)
    joblib.dump(scaler_y, SCALER_Y_PATH)

    print("✅ Modèle et scalers sauvegardés.")
    return model, X_seq