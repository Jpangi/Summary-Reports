import psycopg2
from psycopg2.extras import execute_values

def load(df, db_config):
    print('Loading Data into PostgreSQL')

# convert df to a tuple
    rows = [
        (
            row['control_account'],
            row['work_package'],
            row['cam'],
            row['month_end_date'].date(),
            float(row['hours'])
        )
        for _, row in df.iterrows()
    ]

    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    insert_sql = """
    INSERT INTO cobra
        (control_account, work_package, cam, month_end_date, hours)
        VALUES %s
"""

    execute_values(cursor, insert_sql, rows)
    conn.commit()

    print(f" inserted {cursor.rowcount} rows into 'cobra' table")
    cursor.close()
    conn.close()