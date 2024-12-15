import pandas as pd

def load_and_clean_data(file_path):
    # Load data
    data = pd.read_csv(file_path)

    # Handle missing values
    data.fillna(method='ffill', inplace=True)
    data.fillna(method='bfill', inplace=True)

    # Ensure 'Date' is a datetime object
    if 'Date' in data.columns:
        data['Date'] = pd.to_datetime(data['Date'])
        data.set_index('Date', inplace=True)

    return data
