import pandas as pd

def load_data(path):
    df = pd.read_csv(path)

    df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y-%m-%d %H:%M:%S')
    df = df.sort_values("timestamp").reset_index(drop=True)

    df['side'] = df['percentage'].apply(lambda x: "BUY" if x < 0 else "SELL")

    return df
