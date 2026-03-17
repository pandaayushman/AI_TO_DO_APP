from PySide6.QtWidgets import *
from ai_parser import parse_task
from database import add_task, get_tasks, delete_task, update_task


class TodoWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("AI ToDo Assistant")
        self.resize(400, 500)

        layout = QVBoxLayout()

        self.input = QLineEdit()
        self.input.setPlaceholderText("Study ML tomorrow 6pm")

        self.button = QPushButton("Add Task")
        self.delete_btn = QPushButton("Delete Selected Task")
        self.update_btn = QPushButton("Update Selected Task")

        self.list = QListWidget()

        layout.addWidget(self.input)
        layout.addWidget(self.button)
        layout.addWidget(self.update_btn)
        layout.addWidget(self.delete_btn)
        layout.addWidget(self.list)

        self.setLayout(layout)

        self.button.clicked.connect(self.add_task)
        self.delete_btn.clicked.connect(self.delete_task)
        self.update_btn.clicked.connect(self.update_task)

        self.load_tasks()

    def add_task(self):

        text = self.input.text()

        title, dt = parse_task(text)

        add_task(title, dt)

        self.list.addItem(f"{title} | {dt}")

        self.input.clear()

    def load_tasks(self):

        self.list.clear()

        tasks = get_tasks()

        for t in tasks:
            item = QListWidgetItem(f"{t[1]} | {t[2]}")
            item.setData(1, t[0])
            self.list.addItem(item)

    def delete_task(self):

        item = self.list.currentItem()

        if not item:
            return

        task_id = item.data(1)

        delete_task(task_id)

        self.load_tasks()

    def update_task(self):

        item = self.list.currentItem()

        if not item:
            return

        task_id = item.data(1)

        text = self.input.text()

        title, dt = parse_task(text)

        update_task(task_id, title, dt)

        self.load_tasks()

        self.input.clear()
    
    def closeEvent(self, event):
        event.ignore()
        self.hide()
        