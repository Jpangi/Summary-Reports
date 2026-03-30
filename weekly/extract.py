
import pandas as pd

# ============================================================
# STEP 1: EXTRACT — Read raw data from the CSV
# ============================================================
def extract(filepath):
    print("Extracting data from CSV")
    df = pd.read_csv(filepath)
    print(f"  loaded {len(df)} rows, {len(df.columns)} columns")
    return df
