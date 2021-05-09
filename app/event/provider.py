from app.base.provider import BaseProvider


class Provider(BaseProvider):
    def __int__(self, sql_path):
        super().__init__(sql_path)

    def is_event_exists(self, name):
        return self.exec_by_file('event_exists.sql', {'name': name})[0].get('count')

    def create_event(self, data):
        return self.exec_by_file('create_event.sql', data)[0].get('id')

    def get_event(self, name):
        return self.exec_by_file('get_event.sql', {"name": name})

    def get_events(self):
        return self.exec_by_file('get_events.sql', {})
