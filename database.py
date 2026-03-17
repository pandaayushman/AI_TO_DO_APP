import sqlite3

connection = sqlite3.connect("tasks.db", check_same_thread=False)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
datetime TEXT,
completed INTEGER DEFAULT 0
)
""")

connection.commit()


def add_task(title, datetime):
    cursor.execute(
        "INSERT INTO tasks(title, datetime) VALUES (?, ?)",
        (title, datetime)
    )
    connection.commit()


def get_tasks():
    cursor.execute("SELECT * FROM tasks")
    return cursor.fetchall()


def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    connection.commit()


def update_task(task_id, new_title, new_datetime):
    cursor.execute(
        "UPDATE tasks SET title=?, datetime=? WHERE id=?",
        (new_title, new_datetime, task_id)
    )
    connection.commit()

def mark_completed(task_id):
    cursor.execute(
        "UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,)
    )
    connection.commit()