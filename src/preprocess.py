import pandas as pd

def clean_data(df):
    numeric_columns = [
        "Open",
        "High",
        "Low",
        "Close",
        "Volume"
    ]

    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col])

    df = df.dropna()

    return df