import time
import schedule
from app.config import bot, CHANNEL_LOGIN
from app.event.model import Event
from app.utils.event_parser import CTFTimeParser


def start_parser():
    event = Event()
    parser = CTFTimeParser()

    events = parser.get_events()

    for event_data in events:
        if event.is_exists(event_data['name']):
            continue

        event.add(event_data)

        name = event_data['name'].replace('\'', '')
        date = event_data['date'].replace('\'', '')
        event_format = event_data['format'].replace('\'', '')
        location = event_data['location'].replace('\'', '')
        weight = event_data['weight'].replace('\'', '')
        notes = event_data['notes'].replace('\'', '')
        url = event_data['url'].replace('\'', '')

        msg = f"***Name:*** {name}\n" \
              f"***Date:*** {date}\n" \
              f"***Format:*** {event_format}\n" \
              f"***Location:*** {location}\n" \
              f"***Weight:*** {weight}\n" \
              f"***Notes:*** {notes}\n" \
              f"***More info:*** {url}\n"
        bot.send_message(CHANNEL_LOGIN, msg, parse_mode="Markdown")
        time.sleep(5)


if __name__ == '__main__':
    schedule.every(12).hours.do(start_parser)

    while True:
        schedule.run_pending()
        time.sleep(1)
