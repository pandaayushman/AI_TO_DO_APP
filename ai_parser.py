from datetime import datetime
import dateparser

def parse_task(text):

    if "|" in text:

        title, time_part = text.split("|")

        return title.strip(), time_part.strip()

    dt = dateparser.parse(text)

    if dt is None:
        dt = datetime.now()

    return text, dt.strftime("%Y-%m-%d %H:%M")