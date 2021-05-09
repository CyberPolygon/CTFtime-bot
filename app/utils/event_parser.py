import requests
from bs4 import BeautifulSoup
import urllib3
import lxml


class CTFTimeParser:
    def __init__(self):
        self.response = None
        self.events = None

    def __get_ctftime_content(self, url='https://ctftime.org/event/list/upcoming'):
        urllib3.disable_warnings()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'
        }
        self.response = requests.get(url, verify=False, headers=headers).text

    def __parse_data(self):
        data = []
        for row in self.events:
            if row.find('th'):
                continue

            entities = row.find_all('td')
            link = row.find('a').attrs['href']
            entity_data = []

            for entity in entities:
                text = entity.get_text().replace('\n', '').strip()
                if not text:
                    entity_data.append('Unknown')
                else:
                    entity_data.append(text)

            entity_data.append(f'https://ctftime.org{link}')
            entity_data.pop(-3)
            data.append(entity_data)
        return data

    def __parse_events(self):
        soup = BeautifulSoup(self.response, 'lxml')
        table = soup.find('table', class_='table table-striped')
        self.events = table.find_all('tr')

    def get_events(self):
        self.__get_ctftime_content()
        self.__parse_events()
        return list(
            map(lambda x:
                dict(zip(['name', 'date', 'format', 'location', 'weight', 'notes', 'url'], x)),
                self.__parse_data())
            )


if __name__ == '__main__':
    # CTFTimeParser().get_events()
    for event in CTFTimeParser().get_events():
        print(event)
