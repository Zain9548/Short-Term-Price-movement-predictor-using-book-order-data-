import pandas as pd

def create_features(df):
    buy_depth = df[df["side"] == "BUY"].groupby("timestamp")["depth"].sum()
    sell_depth = df[df["side"] == "SELL"].groupby("timestamp")["depth"].sum()

    feature = pd.concat([buy_depth, sell_depth], axis=1)
    feature.columns = ["total_buy_depth", "total_sell_depth"]

    feature["imbalance"] = (
        (feature["total_buy_depth"] - feature["total_sell_depth"]) /
        (feature["total_buy_depth"] + feature["total_sell_depth"])
    )

    feature["imbalance_lag1"] = feature["imbalance"].shift(1)
    feature["imbalance_avg_5"] = feature["imbalance"].rolling(window=5).mean()
    feature["imbalance_change"] = feature["imbalance"] - feature["imbalance_lag1"]

    feature = feature.dropna()

    return feature
