#loading data

import pandas as pd

def load_dataset(path):
    try:
        data = pd.read_csv(path)
        return data
    except FileNotFoundError:
        print("File not found!")
        return None
