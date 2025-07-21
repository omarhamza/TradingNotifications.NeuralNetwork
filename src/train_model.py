import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
import joblib
from config import SEQ_LEN, MODEL_PATH, features, PRED_HOURS, SCALER_PATH
from send_telegram_message import send_df_via_telegram
from utils import log

def create_sequences(data, seq_len):
    X, y = [], []
    for i in range(len(data) - seq_len):
        X.append(data[i:i + seq_len])
        y.append(data[i + seq_len][0])  # close price
    return np.array(X), np.array(y)

# === Entraînement modèle ===
def train_model(df):
    raw = df[features].values

    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(raw)

    X, _ = create_sequences(scaled, SEQ_LEN)

    y_real = df["close"].values[SEQ_LEN:]
    y_scaled = scaler.fit_transform(y_real.reshape(-1, 1))

    X = X.reshape((X.shape[0], X.shape[1], X.shape[2]))

    model = tf.keras.Sequential([
        tf.keras.layers.LSTM(64, input_shape=(SEQ_LEN, X.shape[2])),
        tf.keras.layers.Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y_scaled, epochs=10, batch_size=32)

    # === Prédictions sur les dernières séquences ===
    last_seq = scaled[-SEQ_LEN:].reshape(1, SEQ_LEN, scaled.shape[1])
    future_predictions = []

    current_seq = last_seq.copy()
    for _ in range(PRED_HOURS):
        pred_scaled = model.predict(current_seq)[0][0]
        future_predictions.append(pred_scaled)

        next_input = np.hstack([pred_scaled] + [current_seq[0, -1, 1:]])
        current_seq = np.append(current_seq[:, 1:], [[next_input]], axis=1)

    # Inverser le scaling uniquement pour 'close'
    dummy_input = np.zeros((len(future_predictions), scaled.shape[1]))
    dummy_input[:, 0] = future_predictions
    preds_real = scaler.inverse_transform(dummy_input)[:, 0]

    # === Timestamps futurs ===
    last_ts = df.index[-1]
    future_times = [last_ts + pd.Timedelta(hours=i + 1) for i in range(PRED_HOURS)]

    df_pred = pd.DataFrame({
        'timestamp': future_times,
        'predicted_close': preds_real
    })
    df_pred['timestamp'] = df_pred['timestamp'].dt.tz_localize('UTC').dt.tz_convert('Etc/GMT-2')
    df_pred.to_csv("eth_predictions.csv", index=False)
    send_df_via_telegram(df_pred)
    print("✅ Prédictions enregistrées dans eth_predictions.csv")

    # Sauvegardes
    model.save(MODEL_PATH)
    joblib.dump(scaler, SCALER_PATH)

    print("✅ Modèle et scalers sauvegardés.")
    return model, X