from ta.momentum import RSIIndicator
from ta.trend import MACD


def add_features(df):

    # Moving averages
    df["MA7"] = df["Close"].rolling(7).mean()

    df["MA30"] = df["Close"].rolling(30).mean()

    # Daily return
    df["Daily_Return"] = df["Close"].pct_change()

    # Volatility
    df["Volatility"] = (
        df["Daily_Return"]
        .rolling(7)
        .std()
    )

    # RSI
    rsi = RSIIndicator(close=df["Close"])

    df["RSI"] = rsi.rsi()

    # MACD
    macd = MACD(close=df["Close"])

    df["MACD"] = macd.macd()

    # Prediction target
    df["Tomorrow"] = df["Close"].shift(-1)

    df["Target"] = (
        df["Tomorrow"] > df["Close"]
    ).astype(int)

    df = df.dropna()

    return df