import pandas as pd

def extract(filepath):
    df = pd.read_csv(filepath)
    print(f"  loaded {len(df)} rows, {len(df.columns)} columns")
    return df