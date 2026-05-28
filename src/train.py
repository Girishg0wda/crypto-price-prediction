from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import joblib
from data_loader import load_data
from preprocess import clean_data
from features import add_features
from evolute import evaluate_model

btc = load_data()

btc = clean_data(btc)

btc = add_features(btc)

features = [
    "Open",
    "High",
    "Low",
    "Close",
    "Volume",
    "MA7",
    "MA30",
    "Daily_Return",
    "Volatility",
    "RSI",
    "MACD"
]

x = btc[features]

y = btc["Target"]

X_train, X_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

evaluate_model(y_test, predictions)

joblib.dump(model, "../models/random_forest.pkl")

print("Model saved successfully!")