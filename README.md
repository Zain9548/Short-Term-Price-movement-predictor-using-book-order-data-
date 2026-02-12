# 🚀 Short-Term Price Movement Predictor using Order Book Data (Live BTCUSDT)


### 🔹 Live Dashboard View
![Dashboard Screenshot](https://github.com/Zain9548/Short-Term-Price-movement-predictor-using-book-order-data-/blob/main/WhatsApp%20Image%202026-02-12%20at%2012.33.31%20PM.jpeg)

### 🔹 Live Signal + Feature Engineering Output
![Signal Screenshot](https://github.com/Zain9548/Short-Term-Price-movement-predictor-using-book-order-data-/blob/main/WhatsApp%20Image%202026-02-12%20at%2012.33.31%20PM.jpeg)


▶️ **Watch Full Demo Video Here:**  
📌 [Click Here to Watch the Demo Video](https://drive.google.com/file/d/1ffSwCCmvpqMVZU91_DmMfVQBi7x_TU4V/view?usp=drive_link)



This project is a **real-time crypto market prediction system** that predicts the **short-term price direction (UP / DOWN)** using **Binance Futures Order Book data**.

It collects live order book updates, performs feature engineering (order book imbalance-based), and uses a trained **Machine Learning model (XGBoost / ML Model)** to generate trading signals.

---

## 📌 Project Objective

The main goal of this project is to predict the **next short-term movement of BTCUSDT price** using **market microstructure data** instead of traditional indicators like RSI or MACD.

This project focuses on **real-time buyer vs seller pressure** using the Binance Futures order book.

---

## 🔥 Key Features

✅ Live BTCUSDT Order Book data using Binance Futures API  
✅ Real-time feature engineering (Imbalance, Lag, Avg, Change)  
✅ ML Model prediction (UP / DOWN)  
✅ Prediction updated every 1 minute  
✅ Live dashboard with professional UI  
✅ Imbalance trend graph  
✅ Prediction history tracking  
✅ Flask REST API for live signal  
✅ Frontend built with HTML, CSS, JavaScript  

---

## 🧠 How It Works (Step-by-Step)

### 1️⃣ Live Order Book Data Fetching
The system connects to Binance Futures order book feed and collects live bids and asks.

### 2️⃣ Feature Engineering
It calculates the following real-time features:

- **Imbalance**  
- **Imbalance Lag1**
- **Imbalance Avg5**
- **Imbalance Change**

- 1. Imbalance

Shows buyer vs seller dominance.

2. Imbalance Lag1

Previous imbalance value.

3. Imbalance Avg5

Moving average of last 5 imbalance values.

4. Imbalance Change

Momentum shift in market pressure.

These features represent market buying/selling pressure.

### 3️⃣ Model Prediction
A trained ML model predicts:

- **UP** → price may increase
- **DOWN** → price may decrease

### 4️⃣ Live API Output
Flask provides a live endpoint:









which returns the latest prediction and features.

### 5️⃣ Dashboard Visualization
Frontend dashboard automatically calls the `/live` API and displays:

- Signal (UP / DOWN)
- Feature values
- Live imbalance graph
- Prediction history

---

## 🛠️ Tech Stack

### Backend:
- Python
- Flask
- Flask-CORS
- Pandas
- Joblib
- XGBoost
- Binance API / Websocket Client

### Frontend:
- HTML
- CSS
- JavaScript
- Chart.js (for graphs)

### Deployment:
- Render Cloud (Backend API)
- But I can not fetech the data using websocket  beacuse websocket live  not a free on render so   i used the local host domain .

---

## 📂 Folder Structure

ShortTerm PriceMovement Predictor/
│
├── backend/
│ ├── app.py
│ ├── requirements.txt
│
├── frontend/
│ ├── index.html
│ ├── style.css
│ ├── script.js
│
├── models/
│ ├── orderbook_model.pkl
│ ├── xgb_orderbook_model.pkl
│
├── realtime/
│ ├── websocket_client.py
│ ├── realtime_predictor.py
│ ├── realtime_feature_engineering.py
│ ├── run_live.py
│ ├── live_logger.py
│
├── logs/
│ └── live_predictions.csv
│
├── data/
│ └── BTCUSDT-bookDepth.csv
│
├── src/
│ ├── train.py
│ ├── evaluate.py
│ ├── feature_engineering.py
│ ├── label_generator.py
│ ├── utils.py
│ ├── config.py
│
├── requirements.txt
└── README.md
