import sqlite3
from datetime import datetime
from config import DB_NAME


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS access_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        uid TEXT NOT NULL,
        status TEXT NOT NULL,
        created_at TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def insert_log(uid, status):
    conn = get_connection()
    cursor = conn.cursor()

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
    INSERT INTO access_logs (uid, status, created_at)
    VALUES (?, ?, ?)
    """, (uid, status, created_at))

    conn.commit()
    conn.close()

def read_logs():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, uid, status, created_at
    FROM access_logs
    ORDER BY id DESC
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows