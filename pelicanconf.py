#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Paul Gowder'
SITENAME = 'Sociological Gobbledygook'
# SITEURL = 'https://sociologicalgobbledygook.com/'

MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./plugins']
PLUGINS = ["render_math", "ipynb.markup"]
IGNORE_FILES = [".ipynb_checkpoints", "*.sqlite3"]
IPYNB_USE_METACELL = True
DISPLAY_PAGES_ON_MENU = False  # KEEP THIS SETTING OR THE SYLLABUS FROM PRIOR YEAR RANDOMLY REAPPEARS (???)

THEME = 'notmyidea-mod'

MATH_JAX={"mathjax_font": "typewriter", 'color':'blue','align':"left"}

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# custom settings from reading docs
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'Lessons'
WITH_FUTURE_DATES = False
NEWEST_FIRST_ARCHIVES = False
ARTICLE_ORDER_BY = 'date'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('University of Iowa College of Law', 'https://law.uiowa.edu/'),
         ('Paul Gowder', 'https://gowder.io'),
         ('Python Documentation', 'http://python.org/'),
         ('Course Github', 'https://github.com/paultopia/gobbledygook'),
         ('UIowa IDAS access', "http://notebooks.hpc.uiowa.edu"),
         ('UIowa IDAS documentation', 'https://wiki.uiowa.edu/display/hpcdocs/Interactive+Data+Analytics+Service+Documentation'),
         ('Lesson Post Tags', 'tags.html'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
