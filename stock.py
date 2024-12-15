import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
def load_data(ticker, start_date, end_date):
    print(f"Fetching data for {ticker} from {start_date} to {end_date}...")
    data = yf.download(ticker, start=start_date, end=end_date)
    print("Columns in the data:", data.columns)
    data.to_csv(f'{ticker}_stock_data.csv')  
    return data
def prepare_data(data, look_back):
    close_prices = data[['Close']].values  
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(close_prices)
    X, y = [], []
    for i in range(look_back, len(scaled_data)):
        X.append(scaled_data[i-look_back:i, 0])  
        y.append(scaled_data[i, 0])  
    X, y = np.array(X), np.array(y)
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))
    return X, y, scaler
def train_lstm_model(X_train, y_train, look_back):
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=False, input_shape=(X_train.shape[1], X_train.shape[2])))
    model.add(Dense(units=1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(X_train, y_train, epochs=10, batch_size=1, verbose=2)
    return model  
def plot_predictions(data, X, y, scaler, model):
    predicted_prices = model.predict(X)
    predicted_prices = scaler.inverse_transform(predicted_prices)
    actual_prices = scaler.inverse_transform(y.reshape(-1, 1))
    plt.figure(figsize=(10, 6))
    plt.plot(actual_prices, label='Actual Prices')
    plt.plot(predicted_prices, label='Predicted Prices')
    plt.title(f"Stock Price Prediction vs Actual Price")
    plt.xlabel("Time")
    plt.ylabel("Stock Price")
    plt.legend()
    plt.show()
def process_multiple_tickers(tickers, start_date, end_date, look_back):
    for ticker in tickers:
        print(f"Processing data for {ticker}...")
        data = load_data(ticker, start_date, end_date)
        X, y, scaler = prepare_data(data, look_back)
        model = train_lstm_model(X, y, look_back)
        plot_predictions(data, X, y, scaler, model)
if __name__ == "__main__":
    tickers = ['AAPL', 'MSFT']  
    start_date = '2020-01-01'
    end_date = '2024-01-01'
    look_back = 10  
    process_multiple_tickers(tickers, start_date, end_date, look_back)
