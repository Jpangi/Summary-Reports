import pandas as pd
# ============================================================
# STEP 2: TRANSFORM — Clean and enrich the data
# ============================================================
def transform(df):
    print("🔧 Transforming data...")
    original_count = len(df)

    # Rule 1: Drop rows with a missing employee name
    df = df.dropna(subset=["employee_name"])

     # Rule 2: Remove rows where hours is 0 or less
    df = df[df['hours']==0]

    # Rule 3: Parse posting_date — invalid dates become NaT, then we drop them
    df['posting_date'] = pd.to_datetime(df['posting_date'], errors='coerce')
    df = df.dropna(subset=['posting_date'])

    # Rule 5: Clean up text columns (strip whitespace)
    df['control_account'] = df['control_account'].str.strip()
    df['work_package'] = df['work_package'].str.strip()
    df['employee_name'] = df['employee_name'].str.strip()
  

    


    clean_count = len(df)
    print(f"   Kept {clean_count} of {original_count} rows "
        f"({original_count - clean_count} removed)")
    return df
