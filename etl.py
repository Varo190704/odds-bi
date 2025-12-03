import pandas as pd
from db import get_connection

LOGS = []

def log(msg):
    LOGS.append(msg)

def run_etl():
    LOGS.clear()
    log("ETL started")

    # Load raw CSV
    df = pd.read_csv("data/raw.csv")   # <- poné acá el nombre que uses realmente
    log(f"Loaded {len(df)} rows from CSV")

    conn = get_connection()
    cur = conn.cursor()

    # Load into raw table
    cur.execute("DELETE FROM rodds")
    df.to_sql("rodds", conn, if_exists="append", index=False)
    log("Raw data inserted")

    # Transform ---------------------------------
    df["time"] = pd.to_datetime(df["time"])
    df["abschange"] = df["liodds"] - df["preodds"]
    df["pctchange"] = (df["abschange"] / df["preodds"]) * 100
    df["volat"] = (df["pctchange"].abs() > 12).astype(int)

    log("Data transformed")

    # Load into clean table
    cur.execute("DELETE FROM codds")
    df.to_sql("codds", conn, if_exists="append", index=False)
    conn.commit()
    conn.close()

    log("Clean data inserted")
    log("ETL completed")

    return LOGS
