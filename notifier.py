from plyer import notification
def send_notification(task):
    notification.notify(
        title = "Task Reminder",
        message = task,
        timeout = 10
    )
