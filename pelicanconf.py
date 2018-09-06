#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Lee Zamparo'
SITENAME = u'Lee Zamparo'
SITEURL = 'http://lzamparo.github.io'
SITESUBTITLE = 'I work on different problems in computational biology.  Main tools are machine learning, Python, R.'
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


# Pelican plugins
MARKUP = ['md']
PLUGIN_PATHS = ['./plugins', '../pelican-plugins']
PLUGINS = ['render_math', 'ipynb.liquid']
IGNORE_FILES = ['.ipynb_checkpoints']

# needed for liquid tags
NOTEBOOK_DIR = 'notebooks'

# Blogroll
LINKS = False 

# Social widget
SOCIAL = False

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

STATIC_PATHS = ['images', 'pdfs']
