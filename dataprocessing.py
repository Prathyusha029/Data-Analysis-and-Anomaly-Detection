import pandas as pd
def load_and_clean_data(file_path):
    data = pd.read_csv(file_path)
    print(data.head())  
    data.ffill(inplace=True)  
    data.bfill(inplace=True)  
    if 'Date' in data.columns:
        data['Date'] = pd.to_datetime(data['Date'])
        data.set_index('Date', inplace=True)
    if 'wt' in data.columns:
        print(f"wt column values:\n{data['wt'].head()}")
    return data
file_path = "C:/Users/Yekam/OneDrive/Desktop/internship2/task3/data.csv"  
data = load_and_clean_data(file_path)
