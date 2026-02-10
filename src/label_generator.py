def create_label(feature_df):
    feature_df["target"] = (
        feature_df["imbalance"].shift(-1) > feature_df["imbalance"]
    ).astype(int)

    feature_df = feature_df.dropna()
    return feature_df
