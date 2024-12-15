import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
file_path = "C:/Users/Yekam/OneDrive/Desktop/internship2/task3/stock_data.csv"
try:
    data = pd.read_csv(file_path, skiprows=2)  
    print("CSV Loaded Successfully")
    print("Columns in the CSV:", data.columns)  
    print("First few rows of the data:\n", data.head())  
except FileNotFoundError as e:
    print(f"Error: The file {file_path} was not found. Please check the file path.")
    print(f"Verbose error: {e}")
    exit()
except ValueError as e:
    print(f"Error loading CSV: {e}")
    print(f"Verbose error: {e}")
    exit()
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    exit()
try:
    data.columns = ['Date', 'Price', 'Adj Close', 'Close', 'High', 'Low', 'Open']
except ValueError as e:
    print(f"Error in renaming columns. Ensure the number of columns matches the provided names.")
    print(f"Verbose error: {e}")
    exit()
try:
    if 'Date' in data.columns:
        data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
        data.set_index('Date', inplace=True)
    else:
        print("Error: 'Date' column not found in the CSV.")
        exit()
except Exception as e:
    print(f"Error in processing the 'Date' column: {e}")
    exit()
print("Cleaned Data:\n", data.head())
def detect_anomalies(data, contamination=0.01):
    try:
        iso_forest = IsolationForest(contamination=contamination, random_state=42)
        anomalies = iso_forest.fit_predict(data[['Close']])
        data['Anomaly'] = anomalies
        plt.figure(figsize=(10, 6))
        plt.plot(data.index, data['Close'], label='Stock Price', alpha=0.7)
        plt.scatter(data.index[data['Anomaly'] == -1], 
                    data['Close'][data['Anomaly'] == -1], 
                    color='red', label='Anomalies')
        plt.legend()
        plt.title('Anomaly Detection')
        plt.show()
        return data
    except KeyError as e:
        print(f"Error: The required column for anomaly detection ('Close') is missing.")
        print(f"Verbose error: {e}")
        exit()
    except Exception as e:
        print(f"An error occurred during anomaly detection: {e}")
        exit()
try:
    data_with_anomalies = detect_anomalies(data)
except Exception as e:
    print(f"An error occurred during the anomaly detection process: {e}")
