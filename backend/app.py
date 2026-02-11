from flask import Flask, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import websocket
import json
from collections import deque
import threading
import time

app = Flask(__name__)
CORS(app)

MODEL_PATH = "backend/models/orderbook_model.pkl"
model = joblib.load(MODEL_PATH)

SOCKET_URL = "wss://fstream.binance.com/ws/btcusdt@depth"

imbalance_window = deque(maxlen=20)
latest_data = {"features": None, "signal": "WAITING"}

# ✅ ADD THIS
last_prediction_time = 0
PREDICT_INTERVAL = 60   # 60 seconds = 1 minute

def compute_features(orderbook_data):
    bids = orderbook_data.get("b", [])
    asks = orderbook_data.get("a", [])

    buy_depth = sum(float(qty) for _, qty in bids)
    sell_depth = sum(float(qty) for _, qty in asks)

    if buy_depth + sell_depth == 0:
        return None

    imbalance = (buy_depth - sell_depth) / (buy_depth + sell_depth)
    imbalance_window.append(imbalance)

    if len(imbalance_window) < 5:
        return None

    lag1 = imbalance_window[-2]
    avg5 = sum(list(imbalance_window)[-5:]) / 5
    change = imbalance - lag1

    return {
        "imbalance": imbalance,
        "imbalance_lag1": lag1,
        "imbalance_avg_5": avg5,
        "imbalance_change": change
    }

def predict_signal(features):
    df = pd.DataFrame([features])
    pred = model.predict(df)[0]
    return "UP" if pred == 1 else "DOWN"

# ✅ UPDATED FUNCTION
def on_message(ws, message):
    global latest_data, last_prediction_time

    data = json.loads(message)

    features = compute_features(data)
    if features is None:
        return

    current_time = time.time()

    # Predict only once per minute
    if current_time - last_prediction_time >= PREDICT_INTERVAL:
        signal = predict_signal(features)

        latest_data["features"] = features
        latest_data["signal"] = signal

        last_prediction_time = current_time

def start_socket():
    ws = websocket.WebSocketApp(SOCKET_URL, on_message=on_message)
    ws.run_forever()

thread = threading.Thread(target=start_socket, daemon=True)
thread.start()

@app.route("/live", methods=["GET"])
def live():
    if latest_data["features"] is None:
        return jsonify({"signal": "WAITING", "features": {}, "time": str(pd.Timestamp.now())})

    return jsonify({
        "signal": latest_data["signal"],
        "features": latest_data["features"],
        "time": str(pd.Timestamp.now())
    })

if __name__ == "__main__":
    app.run(debug=True)
