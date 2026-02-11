from realtime.websocket_client import start_socket
from realtime.realtime_feature_engine import compute_features
from realtime.realtime_predictor import predict_signal
from realtime.live_logger import log_signal

def process_message(orderbook_data):
    features = compute_features(orderbook_data)

    if features is None:
        return

    signal = predict_signal(features)

    print("Live Signal:", signal, "| Imbalance:", features["imbalance"])

    log_signal(signal, features)

start_socket(process_message)
