import pandas as pd

def transform(df):
    print("🔧 Transforming data...")
    original_count = len(df)
     # Rule 1: Drop rows with a missing control account name
    df = df.dropna(subset=['control_account'])

     # Rule 2: Remove rows where hours is 0 or less
    df = df[df['hours'] == 0]

    # Rule 3: Parse posting_date — invalid dates become NaT, then we drop them
    df['month_end_date'] = pd.to_datetime(df['month_end_date'], errors='coerce')
   
    # Rule 5: Clean up text columns (strip whitespace)
    df['control_account'] = df['control_account'].str.strip()
    df['work_package'] = df['work_package'].str.strip()
    df['cam'] = df['cam'].str.strip()
  

    clean_count = len(df)
    print(f"   Kept {clean_count} of {original_count} rows "
        f"({original_count - clean_count} removed)")
    return df
