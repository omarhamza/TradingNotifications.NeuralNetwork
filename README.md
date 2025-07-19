# 📈 Crypto Price Predictor

**Crypto Price Predictor** est une application Python qui prédit le prochain prix d'une cryptomonnaie (comme Bitcoin) à l’aide d’un modèle de réseau de neurones.

---

## 🔍 Fonctionnalités

- 📡 Récupère automatiquement les données de marché depuis l’API Binance toutes les 15 minutes  
- 📊 Calcule des indicateurs techniques comme la moyenne mobile (SMA) et le RSI  
- 🤖 Utilise un modèle LSTM pour prédire le prochain prix basé sur l’historique récent  

---

## 🎯 Objectif

Ce projet est conçu comme une base pour :
- développer des stratégies de trading basées sur l’IA
- apprendre comment appliquer les réseaux de neurones dans le domaine de la finance

---

## 🚧 Statut

Projet en développement local uniquement (pas encore déployé sur le cloud)

---

## 📦 Prérequis

Avant de lancer le projet, assurez-vous d’avoir :

- [Python 3.8+](https://www.python.org/downloads/)

---

### 🛠️ 1. Créer un environnement virtuel (fortement recommandé)
#### ✅ Pour Linux / macOS :
```bash
python -m venv venv
source venv/bin/activate
```

#### ✅ Pour Windows :
```bash
python -m venv venv
venv\Scripts\activate
```

---

### 📥 3. Installer les dépendances
```bash
pip install -r requirements.txt
```