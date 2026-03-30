import psycopg2
from psycopg2.extras import execute_values
# ============================================================
# STEP 3: LOAD — Insert clean data into PostgreSQL
# ============================================================
def load(df, db_config):
    print('Loading data into PostgreSql')

# converts the dataframe into a list of tuples to be uploaded to postgres since SQL can't understand pandas df's.
    rows = [
        (
            row['control_account'],
            row['work_package'],
            row['employee_name'],
            row['posting_date'].date(),
            float(row['hours']),
        )

        
       # since a tuple has both index and data(ex. control account)
       # the _, row unpacks both index and data and grabs only data
        for _, row in df.iterrows()
    ]

    # ** takes a dict and spreads it out into individual arguments
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    insert_sql = """
    INSERT INTO weekly
        (control_account, work_package, employee_name,
        posting_date, hours)
    VALUES %s

    """
    execute_values(cursor, insert_sql, rows)
    conn.commit()

    print(f" inserted {cursor.rowcount} rows into 'weekly' table")
    cursor.close()
    conn.close()