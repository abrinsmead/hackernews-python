import requests


class HackerNews():

    def __init__(self):
        self.url = 'https://hacker-news.firebaseio.com/v0/{uri}'

    def request(self, method, uri):
        url = self.url.format(uri=uri)
        return requests.request(method, url)

    def item(self, item_id):
        r = self.request('GET', 'item/{item_id}.json'.format(item_id=item_id))
        return r.json()

    def user(self, user_id):
        r = self.request('GET', 'user/{user_id}.json'.format(user_id=user_id))
        return r.json()

    def top_stories(self):
        r = self.request('GET', 'topstories.json')
        return r.json()

    def max_item(self):
        r = self.request('GET', 'maxitem.json')
        return r.json()

    def updates(self):
        r = self.request('GET', 'updates.json')
        return r.json()

