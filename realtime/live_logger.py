import csv
import os
from datetime import datetime

LOG_FILE = "logs/live_predictions.csv"

def log_signal(signal, features):
    os.makedirs("logs", exist_ok=True)

    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["time", "signal", "imbalance"])

        writer.writerow([datetime.now(), signal, features["imbalance"]])
