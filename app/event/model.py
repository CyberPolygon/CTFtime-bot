from app.event.provider import Provider


class Event:
    def __init__(self):
        self.provider = Provider()

    def is_exists(self, name):
        return self.provider.is_event_exists(name)

    def add(self, data):
        return self.provider.create_event(data)

    def get_all(self):
        return self.provider.get_events()

    def get(self, name):
        return self.provider.get_event(name)
