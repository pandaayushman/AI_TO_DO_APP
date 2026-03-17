import sqlite3

conn = sqlite3.connect("tasks.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
id INTEGER PRIMARY KEY AUTOINCREMENT,
text TEXT NOT NULL,
time TEXT NOT NULL,
completed INTEGER DEFAULT 0
)
""")

conn.commit()


def add_task(text, time):

    cursor.execute(
        "INSERT INTO tasks(text,time) VALUES(?,?)",
        (text, time)
    )

    conn.commit()


def get_tasks():

    cursor.execute("SELECT * FROM tasks")

    return cursor.fetchall()


def delete_task(task_id):

    cursor.execute(
        "DELETE FROM tasks WHERE id=?",
        (task_id,)
    )

    conn.commit()


def mark_completed(task_id):

    cursor.execute(
        "UPDATE tasks SET completed=1 WHERE id=?",
        (task_id,)
    )

    conn.commit()