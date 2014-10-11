Hacker News API Wrapper
=======================

Installation
------------

.. code-block:: bash

    pip install hackernews-python

Usage
-----

.. code-block:: pycon

    >>> from hackernews import HackerNews
    >>> hn = HackerNews()
    >>> hn.top_stories()
    [8422599, 8422087, 8422928, 8422581, 8423825...

    >>> hn.user('pg')
    {'delay': 2, 'id': 'pg', 'submitted': [7494555, 7494520, 749411...

    >>> hn.user('pg')['created']
    datetime.datetime(2006, 10, 9, 11, 21, 32)

    >>> hn.item(1)['title']
    'Y Combinator'

    >>> hn.item(1)['time']
    datetime.datetime(2006, 10, 9, 11, 21, 51)

    >>> hn.max_item()
    8424314

    >>> hn.updates()
    {'items': [8423690, 8424315, 8424299...], 'profiles': ['exampleuser',...]}


API Documentation
-----------------

https://github.com/HackerNews/API

