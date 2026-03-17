import sys
import threading
import time
from datetime import datetime, timedelta

from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from gui import TodoWindow
from database import get_tasks, mark_completed
from notifier import send_notification
from PySide6.QtGui import QPalette, QColor, QAction, QIcon

def dark_theme(app):

    palette = QPalette()

    palette.setColor(QPalette.Window, QColor(53,53,53))
    palette.setColor(QPalette.WindowText, QColor(255,255,255))
    palette.setColor(QPalette.Base, QColor(25,25,25))
    palette.setColor(QPalette.AlternateBase, QColor(53,53,53))
    palette.setColor(QPalette.ToolTipBase, QColor(255,255,255))
    palette.setColor(QPalette.ToolTipText, QColor(255,255,255))
    palette.setColor(QPalette.Text, QColor(255,255,255))
    palette.setColor(QPalette.Button, QColor(53,53,53))
    palette.setColor(QPalette.ButtonText, QColor(255,255,255))
    palette.setColor(QPalette.Highlight, QColor(142,45,197))
    palette.setColor(QPalette.HighlightedText, QColor(255,255,255))

    app.setPalette(palette)

def reminder_loop():

    while True:

        tasks = get_tasks()

        now = datetime.now()

        for task in tasks:

            task_id = task[0]
            title = task[1]
            task_time_str = task[2]
            completed = task[3]


            task_time = datetime.strptime(task_time_str, "%Y-%m-%d %H:%M")

            if task_time <= now and completed == 0:

                send_notification(title)
                mark_completed(task_id)

        time.sleep(60)
    


app = QApplication(sys.argv)

window = TodoWindow()
window.show()
tray = QSystemTrayIcon()
tray.setIcon(QIcon("download.png"))  # you can add an icon file later

menu = QMenu()

open_action = QAction("Open")
quit_action = QAction("Quit")

open_action.triggered.connect(window.show)
quit_action.triggered.connect(app.quit)

menu.addAction(open_action)
menu.addAction(quit_action)

tray.setContextMenu(menu)
tray.show()
app.setStyle("Fusion")
dark_theme(app)

threading.Thread(target=reminder_loop, daemon=True).start()

sys.exit(app.exec())