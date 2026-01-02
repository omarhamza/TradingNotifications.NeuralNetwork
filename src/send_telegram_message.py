import requests
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

def notify(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    title = "--*Neural network*--"
    full_message = f"{title}\n{message}"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": full_message,
        "parse_mode": "Markdown"
    }
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print("Erreur envoi Telegram :", e)

def buy_notification(symbol, score):
    notify(f"""🚀 *Signal d'achat détecté !*
Il est peut-être temps d'acheter *{symbol}*
Score: {score} !""")

def sell_notification(symbol, score):
    notify(f"""📉🔥 *Signal de vente détecté !*
Il est peut-être temps de vendre *{symbol}*
Score: {score} !""")
    

def send_df_via_telegram(df, symbol):
    # Limite le nombre de lignes si besoin
    df_to_send = df[['timestamp', 'predicted_close']].copy()

    # Convertit le timestamp en chaîne (optionnel, format lisible)
    df_to_send['timestamp'] = df_to_send['timestamp'].dt.strftime("%Y-%m-%d %H:%M")

    # Formate chaque ligne : **timestamp** : **predicted_close**
    rows = [
        f"*{row['timestamp']}* : *{row['predicted_close']:.2f}*"
        for _, row in df_to_send.iterrows()
    ]

    message = f"📊 *Prédiction prix clos {symbol}* \n\n" + "\n".join(rows)

    print(f"📊 *Prédiction prix clos {symbol}* \n\n")

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }

    try:
        requests.post(url, data=payload)
        print("✅ Message envoyé sur Telegram.")
    except Exception as e:
        print("❌ Erreur envoi Telegram:", e)