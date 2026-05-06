import sqlite3
from datetime import datetime

DB_PATH = "/app/data/tasks.db"


def get_conn():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
    create table if not exists tasks(
        id integer primary key autoincrement,
        task_id text,     
        status text,     
        result text,     
        created_at text     
    )
    """)

    conn.commit()
    conn.close()


def create_task_record(task_id: str):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute(
        "insert into tasks (task_id, status, created_at) values (?,?,?)",
        (task_id, "PENDING", datetime.now().isoformat())
    )

    conn.commit()
    conn.close()


def update_task_record(task_id: str, status: str, result: str = None):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute(
        "update tasks set status = ?, result = ? where task_id = ?",
        (status, result, task_id)
    )

    conn.commit()
    conn.close()


def get_task_record(task_id: str):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute(
        "select task_id, status, result from tasks where task_id = ?",
        (task_id,)
    )

    row = cursor.fetchone() 
    conn.close()

    return row