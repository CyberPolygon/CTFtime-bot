from event.provider import Provider


class Event:
    def __init__(self):
        self.provider = Provider()

    def is_exists(self, event):
        name = event['name']
        url = event['url']
        return self.provider.is_event_exists(name, url)

    def add(self, data):
        return self.provider.create_event(list(data.values()))

    def get_all(self):
        return self.provider.get_events()

    def get(self, name):
        return self.provider.get_event(name)
