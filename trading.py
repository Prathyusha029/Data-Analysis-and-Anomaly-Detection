import pandas as pd
import matplotlib.pyplot as plt
def generate_trading_signals(data):
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    data['SMA_200'] = data['Close'].rolling(window=200).mean()
    data['Signal'] = 0
    data.loc[data['SMA_50'] > data['SMA_200'], 'Signal'] = 1  
    data.loc[data['SMA_50'] < data['SMA_200'], 'Signal'] = -1  
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Close'], label='Stock Price')
    plt.plot(data.index, data['SMA_50'], label='50-Day SMA')
    plt.plot(data.index, data['SMA_200'], label='200-Day SMA')
    plt.scatter(data.index[data['Signal'] == 1], data['Close'][data['Signal'] == 1], label='Buy Signal', color='green', marker='^')
    plt.scatter(data.index[data['Signal'] == -1], data['Close'][data['Signal'] == -1], label='Sell Signal', color='red', marker='v')
    plt.legend()
    plt.title('Stock Trading Signals')
    plt.show()
file_path = "C:/Users/Yekam/OneDrive/Desktop/internship2/task3/data.csv"  
data = pd.read_csv(file_path)
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)
generate_trading_signals(data)
