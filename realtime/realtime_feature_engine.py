from collections import deque

imbalance_window = deque(maxlen=10)

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
