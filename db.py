import sqlite3

DB_NAME = "odds.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS rodds (
            matchid INTEGER,
            matchname TEXT,
            time TEXT,
            preodds REAL,
            liodds REAL,
            PRIMARY KEY (matchid, time)
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS codds (
            matchid INTEGER,
            matchname TEXT,
            time TEXT,
            preodds REAL,
            liodds REAL,
            abschange REAL,
            pctchange REAL,
            volat INTEGER,
            PRIMARY KEY (matchid, time)
        )
    """)

    conn.commit()
    conn.close()
