import time
import schedule
from config import bot, CHANNEL_LOGIN
from event.model import Event
from utils.event_parser import CTFTimeParser


def start_parser():
    event = Event()
    parser = CTFTimeParser()

    events = parser.get_events()

    for event_data in events:
        if event.is_exists(event_data):
            continue

        event.add(event_data)

        name = event_data['name']
        date = event_data['date']
        event_format = event_data['format']
        location = event_data['location']
        weight = event_data['weight']
        notes = event_data['notes']
        url = event_data['url']

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
