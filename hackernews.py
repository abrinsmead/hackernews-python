
__version__ = '0.3.2'

from datetime import datetime

import requests


class Item():
    def __init__(self, **entries):
        self.__dict__.update(entries)


class User():
    def __init__(self, **entries):
        self.__dict__.update(entries)


class HackerNews():

    def __init__(self, timeout=5):
        self.url = 'https://hacker-news.firebaseio.com/v0/{uri}'
        self.timeout = timeout

    def request(self, method, uri):
        url = self.url.format(uri=uri)
        return requests.request(method, url, timeout=self.timeout)

    def item(self, item_id):
        uri = 'item/{item_id}.json'.format(item_id=item_id)
        response = self.request('GET', uri)
        item = response.json()
        if item.get('time'):
            item['time'] = datetime.fromtimestamp(item['time'])
        return Item(**item)

    def user(self, user_id):
        uri = 'user/{user_id}.json'.format(user_id=user_id)
        response = self.request('GET', uri)
        user = response.json()
        user['created'] = datetime.fromtimestamp(user['created'])
        return User(**user)

    def top_stories(self):
        response = self.request('GET', 'topstories.json')
        return response.json()

    def max_item(self):
        response = self.request('GET', 'maxitem.json')
        return response.json()

    def updates(self):
        response = self.request('GET', 'updates.json')
        return response.json()

