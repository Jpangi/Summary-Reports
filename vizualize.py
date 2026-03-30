import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
from weekly.config import DB_CONFIG

def fetch_data(db_config):
    conn = psycopg2.connect(**db_config)

    # Query weekly table
    weekly_df = pd.read_sql("""
    SELECT
        control_account,
        work_package,
        employee_name AS name,
        hours,
        posting_date AS date
    FROM weekly
    """, conn)
    weekly_df['source'] = 'weekly'
    
    # Query cobra table
    cobra_df = pd.read_sql("""
    SELECT
        control_account,
        work_package,
        cam,
        hours,
        month_end_date AS date
    FROM cobra
    """, conn)
    cobra_df['source'] = 'cobra'

    df = pd.concat([weekly_df, cobra_df], ignore_index=True)
    print(f"   Combined {len(df)} total rows")
    return df


# Hours by control account
def chart_hours_by_control_account(df):
    data = df.groupby("control_account")["hours"].sum().sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(data.index, data.values, color="steelblue")
    ax.set_title("Total Hours by Control Account", fontsize=14, fontweight="bold")
    ax.set_xlabel("Control Account")
    ax.set_ylabel("Total Hours")
    ax.tick_params(axis="x", rotation=45)
    plt.tight_layout()
    plt.savefig("chart_control_account.png")
    print("   ✅ Saved chart_control_account.png")
    plt.show()

# ============================================================
#  CHART 2 — Hours by Work Package
# ============================================================
def chart_hours_by_work_package(df):
    data = df.groupby("work_package")["hours"].sum().sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(data.index, data.values, color="darkorange")
    ax.set_title("Total Hours by Work Package", fontsize=14, fontweight="bold")
    ax.set_xlabel("Work Package")
    ax.set_ylabel("Total Hours")
    ax.tick_params(axis="x", rotation=45)
    plt.tight_layout()
    plt.savefig("chart_work_package.png")
    print("   ✅ Saved chart_work_package.png")
    plt.show()


# ============================================================
# CHART 3 — Hours by Source
# ============================================================
def chart_hours_over_time(df):
    # Make sure date column is a proper datetime
    df["date"] = pd.to_datetime(df["date"])

    # Group by date and sum hours
    data = df.groupby("date")["hours"].sum().sort_index()

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(data.index, data.values, color="steelblue")
    ax.set_title("Total Hours Over Time", fontsize=14, fontweight="bold")
    ax.set_xlabel("Date")
    ax.set_ylabel("Total Hours")
    ax.tick_params(axis="x", rotation=45)
    plt.tight_layout()
    plt.savefig("chart_hours_over_time.png")
    print("   ✅ Saved chart_hours_over_time.png")
    plt.show()

if __name__ == "__main__":
    df = fetch_data(DB_CONFIG)

    print("\n📊 Generating charts...")
    chart_hours_by_control_account(df)
    chart_hours_by_work_package(df)
    chart_hours_over_time(df)

    print("\n🎉 All charts generated!")