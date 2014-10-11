from datetime import datetime

import requests


class HackerNews():

    def __init__(self, timeout=5):
        self.url = 'https://hacker-news.firebaseio.com/v0/{uri}'
        self.timeout = timeout

    def request(self, method, uri):
        url = self.url.format(uri=uri)
        return requests.request(method, url, timeout=self.timeout)

    def item(self, item_id):
        r = self.request('GET', 'item/{item_id}.json'.format(item_id=item_id))
        item = r.json()
        item['time'] = datetime.fromtimestamp(item['time'])
        return item

    def user(self, user_id):
        r = self.request('GET', 'user/{user_id}.json'.format(user_id=user_id))
        user = r.json()
        user['created'] = datetime.fromtimestamp(user['created'])
        return user

    def top_stories(self):
        r = self.request('GET', 'topstories.json')
        return r.json()

    def max_item(self):
        r = self.request('GET', 'maxitem.json')
        return r.json()

    def updates(self):
        r = self.request('GET', 'updates.json')
        return r.json()
