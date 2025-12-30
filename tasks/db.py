# tasks/db.py
import sqlite3
from django.conf import settings
from datetime import date

DB_PATH = settings.BASE_DIR / "db.sqlite3"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def create_tasks_table():
    query = """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        due_date TEXT,
        status TEXT DEFAULT 'PENDING'
    );
    """
    conn = get_connection()
    conn.execute(query)
    conn.commit()
    conn.close()


def create_task(title, description, due_date, status="PENDING"):
    query = """
    INSERT INTO tasks (title, description, due_date, status)
    VALUES (?, ?, ?, ?)
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, (title, description, due_date, status))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return task_id


def get_all_tasks():
    query = "SELECT * FROM tasks ORDER BY id DESC"
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]
