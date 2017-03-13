#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Scott Newman'
SITENAME = u'Finance Data Geek'
SITEURL = 'http://www.financedatageek.com'

PATH = 'content'

TIMEZONE = 'US/Mountain'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_RSS = "feed.xml"
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

THEME = 'themes/bluegreen'

# Use the content file's basename as the slug when generating output files
SLUGIFY_SOURCE = 'basename'

# Don't write these pages
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
METADATA_SAVE_AS = ''

ARTICLE_URL = '{slug}.html'
ARTICLE_SAVE_AS = '{slug}.html'

# Set the name of the ouptut directory where static files are written
THEME_STATIC_DIR = 'static'

# Delete everything in the output directory when generating
DELETE_OUTPUT_DIRECTORY = True

STATIC_PATHS = ['extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

DEFAULT_DATE_FORMAT = '%B %d, %Y'