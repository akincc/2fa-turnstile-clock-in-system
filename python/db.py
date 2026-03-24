import sqlite3
from datetime import datetime
from config import DB_NAME, allowed_uids


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        uid TEXT NOT NULL UNIQUE,
        name TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS access_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        uid TEXT NOT NULL,
        name TEXT NOT NULL,
        status TEXT NOT NULL,
        created_at TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def insert_user(uid, name):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT OR IGNORE INTO users (uid, name)
        VALUES (?, ?)
        """, (uid, name))

        conn.commit()
        conn.close()


def get_user_name(uid):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT name FROM users
    WHERE uid = ?
    """, (uid,))

    row = cursor.fetchone()
    conn.close()

    if row:
        return row[0]
    return "Unknown"


def insert_log(uid, status):
    conn = get_connection()
    cursor = conn.cursor()

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
    INSERT INTO access_logs (uid, name, status, created_at)
    VALUES (?, ?, ?, ?)
    """, (uid, get_user_name(uid),  status, created_at))

    conn.commit()
    conn.close()


def read_logs():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT access_logs.id, access_logs.uid, access_logs.name, access_logs.status, access_logs.created_at
    FROM access_logs
    ORDER BY access_logs.id DESC
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows