from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QListWidget,
    QMessageBox
)

from database import add_task, get_tasks, delete_task
from ai_parser import parse_task


class TodoWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("AI ToDo Manager")
        self.setMinimumSize(400, 500)

        layout = QVBoxLayout()

        self.input = QLineEdit()
        self.input.setPlaceholderText("Example: study ML tomorrow at 8pm")

        self.add_btn = QPushButton("Add Task")

        self.task_list = QListWidget()

        self.delete_btn = QPushButton("Delete Selected Task")

        layout.addWidget(self.input)
        layout.addWidget(self.add_btn)
        layout.addWidget(self.task_list)
        layout.addWidget(self.delete_btn)

        self.setLayout(layout)

        self.add_btn.clicked.connect(self.add_task_gui)
        self.delete_btn.clicked.connect(self.delete_task_gui)

        self.load_tasks()

    def load_tasks(self):

        self.task_list.clear()

        tasks = get_tasks()

        for task in tasks:
            self.task_list.addItem(f"{task[1]}  |  {task[2]}")

    def add_task_gui(self):

        text = self.input.text()

        task_text, task_time = parse_task(text)

        if task_time is None:
            QMessageBox.warning(
                self,
                "Time not detected",
                "Example:\nStudy ML tomorrow at 8pm\nCall mom in 2 hours"
            )
            return

        task_time_str = task_time.strftime("%Y-%m-%d %H:%M")

        add_task(task_text, task_time_str)

        self.input.clear()

        self.load_tasks()

    def delete_task_gui(self):

        selected = self.task_list.currentRow()

        if selected < 0:
            return

        tasks = get_tasks()

        task_id = tasks[selected][0]

        delete_task(task_id)

        self.load_tasks()