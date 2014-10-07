Hacker News API Wrapper
=======================

Installation
------------

.. code-block::

    pip install hackernews-python

Usage
-----

.. code-block::

    >>> from hackernews import HackerNews
    >>> hn = HackerNews()
    >>> hn.top_stories()
    [8422599, 8422087, 8422928, 8422581, 8423825...

    >>> hn.user('pg')
    {'delay': 2, 'id': 'pg', 'submitted': [7494555, 7494520, 749411...

    >>> hn.item(7494555)['title'])
    Hacker News API

    >>> hn.max_item()
    8424314

    >>> hn.updates()
    {'items': [8423690, 8424315, 8424299...], 'profiles': ['exampleuser',...]}



