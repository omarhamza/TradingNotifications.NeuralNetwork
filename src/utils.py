import os
import glob
from config import TIMEFRAME
from send_telegram_message import notify

def log(msg):
    print(f"[LOG] {msg}")

def trace(msg):
    print(f"[TRACE] {msg}")
    
def error(msg):
    print(f"[ERROR] {msg}")

def normalize_array(arr):
    min_val = arr.min()
    max_val = arr.max()
    norm = (arr - min_val) / (max_val - min_val)
    return norm, min_val, max_val

# ---------------------- Sauvegarder dans un CSV ---------------------- #
def save_to_csv(df, symbol):
    # -------- delete all csv files before create new ones
    delete_csv_files()
    filename = f"historical_{symbol.replace('/', '')}_{TIMEFRAME}.csv"
    df.to_csv(filename)
    print(f"✅ Données sauvegardées dans {filename}")

# ---------------------- Supprimer tous les fichiers .csv dans le répertoire courant -------------------- #
def delete_csv_files():
    for file in glob.glob("*.csv"):
        try:
            os.remove(file)
            print(f"✅ Supprimé : {file}")
        except Exception as e:
            notify(f"❌❌❌ Erreur globale : {e}")