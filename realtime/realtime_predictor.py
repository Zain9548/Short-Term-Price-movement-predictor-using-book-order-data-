import joblib
import pandas as pd

MODEL_PATH = "models/xgb_orderbook_model.pkl"
model = joblib.load(MODEL_PATH)

def predict_signal(features):
    df = pd.DataFrame([features])
    pred = model.predict(df)[0]

    return "UP" if pred == 1 else "DOWN"
