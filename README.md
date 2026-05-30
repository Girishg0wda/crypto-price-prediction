🚀 Cryptocurrency Price Prediction Dashboard

A Machine Learning-powered web application that predicts Bitcoin market trends using technical indicators and historical cryptocurrency data. The project demonstrates the complete ML lifecycle, including data preprocessing, feature engineering, model training, evaluation, and deployment through a Streamlit dashboard.

🌐 Live Demo
https://crypto-price-prediction-girishg0wda.streamlit.app/

📌 Overview
Cryptocurrency markets are highly volatile and difficult to predict. This project leverages Machine Learning and Technical Analysis indicators to identify potential Bitcoin price movement patterns.
The application processes historical market data, generates technical indicators, trains a Random Forest classifier, and provides trend predictions through an interactive dashboard.

✨ Features
* 📈 Bitcoin trend prediction (UP/DOWN)
* 🤖 Random Forest Machine Learning model
* 📊 Technical Analysis indicators:
  * RSI (Relative Strength Index)
  * MACD (Moving Average Convergence Divergence)
  * Moving Averages
  * Volatility
* 📉 Interactive Streamlit dashboard
* 📋 Model evaluation metrics
* 🔄 Automated data preprocessing pipeline
* 📦 Modular project structure

🛠 Tech Stack
Programming & Data Analysis
* Python
* Pandas
* NumPy

Machine Learning
* Scikit-learn
* Random Forest Classifier
* Joblib

Technical Analysis
* TA Library

Visualization
* Streamlit
* Matplotlib
* Seaborn
* Plotly

Version Control & Deployment
* Git
* GitHub
* Streamlit Cloud

```
## 📂 Project Structure

crypto-price-prediction/
│
├── app/
│   └── app.py
│
├── data/
│   └── BTC-USD.csv
│
├── models/
│   └── random_forest.pkl
│
├── src/
│   ├── data_loader.py
│   ├── features.py
│   ├── preprocess.py
│   ├── train.py
│
├── screenshots/
│
├── requirements.txt
├── README.md
└── .gitignore
```


⚙️ Installation

Clone Repository
git clone https://github.com/Girishg0wda/crypto-price-prediction.git

Navigate to Project
cd crypto-price-prediction

Install Dependencies
pip install -r requirements.txt

Run Application
python -m streamlit run app/app.py

🧠 Machine Learning Pipeline

1. Data Collection
* Historical Bitcoin market data loaded from CSV dataset.

2. Data Preprocessing
* Missing value handling
* Data cleaning
* Feature preparation

3. Feature Engineering
Generated indicators:
* Daily Return
* Moving Average (7-Day)
* Moving Average (30-Day)
* RSI
* MACD
* Volatility

4. Model Training
* Random Forest Classifier
* Train/Test Split
* Model Serialization using Joblib

5. Model Evaluation
Performance measured using:
* Accuracy
* Precision
* Recall
* F1-Score

6. Deployment
* Streamlit Dashboard
* GitHub Version Control
* Streamlit Cloud Hosting

📊 Model Performance
| Metric    | Score   |
| --------- | ------- |
| Accuracy  | ~48-50% |
| Precision | ~48%    |
| Recall    | ~50%    |
| F1-Score  | ~49%    |

Note: Cryptocurrency markets are highly stochastic and difficult to predict. Even modest predictive performance can provide valuable insights when combined with risk management strategies.

🚀 Future Improvements
* XGBoost implementation
* Hyperparameter optimization
* LSTM Deep Learning models
* Real-time cryptocurrency data
* Binance API integration
* Sentiment Analysis using Twitter/Reddit
* Multi-cryptocurrency support
* Trading signal generation

🎯 Key Learning Outcomes
This project demonstrates practical experience in:
* Machine Learning model development
* Feature engineering
* Technical Analysis indicators
* Model evaluation techniques
* Git & GitHub workflows
* Streamlit application development
* Cloud deployment
* Real-world debugging and dependency management

👨‍💻 Author
Girish Gowda
GitHub:
https://github.com/Girishg0wda

LinkedIn:
https://www.linkedin.com/in/girisha-s-r

⭐ Support
If you found this project useful, consider giving it a ⭐ on GitHub.
