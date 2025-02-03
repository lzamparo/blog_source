#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Lee'
SITENAME = u'Lee Zamparo'
SITEURL = "http://localhost:8000"
SITETITLE = "Lee Zamparo"
SITELOGO = "/images/profile.png"
SITESUBTITLE = "machine learning, computational biology, NLP"

# Pelican theme
THEME = "themes/Flex"
PATH = "content"
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''

TIMEZONE = 'America/New_York'
I18N_TEMPLATES_LANG = "en"
DEFAULT_LANG = "en"
OG_LOCALE = "en_US"
LOCALE = "en_US"

DATE_FORMATS = {
    "en": "%B %d, %Y",
}


# paths beneath $PATH
STATIC_PATHS = ['images', 'pdfs']

# Flex specific variables
# Main Menu Items
MAIN_MENU = False
#MENUITEMS = (
#    ('Blog', '/'), 
#    ('CV', '/pdfs/lee_cv.pdf')
#)

SOCIAL = (
    ('github', 'https://github.com/lzamparo'),
    ('envelope', 'mailto:zamparo@gmail.com'),
    ('linkedin', 'https://www.linkedin.com/in/lee-zamparo'),
    ('scholar', 'https://scholar.google.ca/citations?user=UtAt8MoAAAAJ'),
)


THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = False
USE_LESS = True

# Pelican plugins
MARKUP = ['md']
PLUGIN_PATHS = ['./plugins']

from pelican_jupyter import liquid as nb_liquid
PLUGINS = ['render_math', 'pelican.plugins.liquid_tags', nb_liquid]
IGNORE_FILES = ['.ipynb_checkpoints']

# needed for liquid tags
NOTEBOOK_DIR = 'notebooks'
DEFAULT_PAGINATION = 2
