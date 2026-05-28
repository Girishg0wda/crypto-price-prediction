import yfinance as yf

def load_data():
    btc = yf.download(
        "BTC-USD",
        start = "2020-01-01",
        end = "2025-01-01"
    )

    btc.columns = btc.columns.get_level_values(0)
    return btc