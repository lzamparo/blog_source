#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Lee Zamparo'
SITENAME = u'Lee Zamparo'
SITEURL = 'http://lzamparo.github.io'
SITESUBTITLE = '1. Get the data 2. Learn a model 3. ??? 4. Knowledge'
PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Pelican theme
THEME = 'crowsfoot'

# Crowsfoot specific variables
PROFILE_IMAGE_URL='https://en.gravatar.com/userimage/6827348/8ddec1ea955824dea50c908ad3154623.png?size=200'
EMAIL_ADDRESSS='zamparol@cbio.mskcc.org'
GITHUB_ADDRESS='https://github.com/lzamparo'
TWITTER_ADDRESS='https://twitter.com/lzamparo'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Menu items for 
MENUITEMS = [('Blog', '/'), ('CV', '/pdfs/lee_cv.pdf')]

# Ensure both .md and .ipynb get taken as content
MARKUP = ('md', 'ipynb')

# Pelican plugins
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ["render_math", "ipynb"]

# Blogroll
LINKS = False 

# Social widget
SOCIAL = False

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

STATIC_PATHS = ['images', 'pdfs']
