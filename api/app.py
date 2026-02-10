from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("models/orderbook_model.pkl")

@app.route("/")
def home():
    return "Order Book Predictor API Running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    df = pd.DataFrame([data])

    pred = model.predict(df)[0]
    signal = "UP" if pred == 1 else "DOWN"

    return jsonify({"prediction": signal})

if __name__ == "__main__":
    app.run(debug=True)
