import dateparser
from dateparser.search import search_dates
from datetime import datetime


def parse_task(text):

    result = search_dates(
        text,
        settings={
            "PREFER_DATES_FROM": "future",
            "RELATIVE_BASE": datetime.now()
        }
    )

    if result is None:
        return text, None

    # first detected date
    detected_text, detected_date = result[0]

    # remove the detected time phrase from task
    task_text = text.replace(detected_text, "").strip()

    if task_text == "":
        task_text = text

    return task_text, detected_date