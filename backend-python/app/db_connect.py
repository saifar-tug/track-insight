import pandas as pd
import os

def fetch_table(table_name):
    csv_path = os.path.join("mock_data", f"{table_name}.csv")
    if os.path.exists(csv_path):
        print(f"Reading {table_name} from local CSV...")
        return pd.read_csv(csv_path)
    else:
        raise FileNotFoundError(f"No local CSV found for {table_name}")
