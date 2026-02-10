import joblib
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

from src.data_loader import load_data
from src.feature_engineering import create_features
from src.label_generator import create_label
from src.evaluate import evaluate_model

DATA_PATH = "data/BTCUSDT-bookDepth.csv"
MODEL_PATH = "models/xgb_orderbook_model.pkl"

df = load_data(DATA_PATH)
feature = create_features(df)
feature = create_label(feature)

X = feature[["imbalance", "imbalance_lag1", "imbalance_avg_5", "imbalance_change"]]
y = feature["target"]

split = int(len(feature) * 0.7)

X_train = X.iloc[:split]
y_train = y.iloc[:split]

X_test = X.iloc[split:]
y_test = y.iloc[split:]

model = XGBClassifier(
    n_estimators=300,
    max_depth=4,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
    eval_metric="logloss"
)

model.fit(X_train, y_train)

evaluate_model(model, X_test, y_test)

joblib.dump(model, MODEL_PATH)
print("Model saved to:", MODEL_PATH)
