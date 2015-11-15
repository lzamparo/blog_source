#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Lee Zamparo'
SITENAME = 'Lee Zamparo'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = 'en'

# Pelican theme
THEME = './crowsfoot'

# Crowsfoot specific variables
PROFILE_IMAGE_URL='images/me.png'
EMAIL_ADDRESSS='zamparol@cbio.mskcc.org'
GITHUB_ADDRESS='https://github.com/lzamparo'
TWITTER_ADDRESS='https://twitter.com/lzamparo'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/lzamparo/'),
          ('Twitter', 'https://twitter.com/lzamparo'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
