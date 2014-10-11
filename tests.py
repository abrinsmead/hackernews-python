from datetime import datetime
import unittest

from requests.exceptions import ConnectTimeout

from hackernews import HackerNews


class HackerNewsTestCase(unittest.TestCase):

    def setUp(self):
        self.hn = HackerNews()

    def test_top_story_count(self):
        top_stories = self.hn.top_stories()
        self.assertEqual(len(top_stories), 100)

    def test_max_item_positive_integer(self):
        max_item = self.hn.max_item()
        self.assertGreaterEqual(max_item, 0)

    def test_updates_result_is_dict(self):
        updates = self.hn.updates()
        self.assertIsInstance(updates, dict)

    def test_item_result_is_dict(self):
        item = self.hn.item(1)
        self.assertIsInstance(item, dict)

    def test_user_result_is_dict(self):
        item = self.hn.user('pg')
        self.assertIsInstance(item, dict)

    def test_user_created_is_datetime(self):
        item = self.hn.user('pg')
        self.assertIsInstance(item['created'], datetime)

    def test_item_time_is_datetime(self):
        item = self.hn.item('1')
        self.assertIsInstance(item['time'], datetime)

    def test_raises_connection_timeout(self):
        hn = HackerNews(timeout=1)
        hn.url = "http://192.0.2.0"  # RFC 5735 TEST-NET-1
        self.assertRaises(ConnectTimeout, hn.top_stories)

