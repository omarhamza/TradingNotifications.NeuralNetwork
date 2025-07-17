import requests
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID, SYMBOL

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

def buy_notification(symbol=SYMBOL):
    notify(f"Buy {symbol}")

def sell_notification(symbol=SYMBOL):
    notify(f"Sell {symbol}")