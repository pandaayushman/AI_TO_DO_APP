import sys
import threading
import time
from datetime import datetime

from PySide6.QtWidgets import QApplication
from gui import TodoWindow
from database import get_tasks, mark_completed
from notifier import send_notification


def reminder_loop():

    while True:

        tasks = get_tasks()

        for task in tasks:

            task_id = task[0]
            task_text = task[1]
            task_time = task[2]
            completed = task[3]

            if completed:
                continue

            task_dt = datetime.strptime(task_time, "%Y-%m-%d %H:%M")

            if datetime.now() >= task_dt:
                send_notification("Reminder", task_text)
                mark_completed(task_id)

        time.sleep(60)


def main():

    app = QApplication(sys.argv)

    window = TodoWindow()
    window.show()

    thread = threading.Thread(target=reminder_loop, daemon=True)
    thread.start()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()