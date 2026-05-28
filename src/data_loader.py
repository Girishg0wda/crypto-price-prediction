import pandas as pd


def load_data():

    btc = pd.read_csv(
        "../data/BTC-USD.csv",
        sep=";"
    )

    btc["timestamp"] = pd.to_datetime(
        btc["timestamp"]
    )

    btc.set_index(
        "timestamp",
        inplace=True
    )

    return btc