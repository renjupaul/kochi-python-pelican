#!/usr/bin/env python
# -*- coding:utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jasim Muhammed'
SITENAME = u'Kochi Python'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Calcutta'

READERS = {
    'html':None
}

STATIC_PATHS = ['images', 'slides']

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
# COVER_IMG = https://pbs.twimg.com/profile_background_images/483590998014980096/T1MRguut.jpeg"
COVER_BG_COLOR = "#2b5b84"
COVER_IMG = "linear-gradient(#1e415e 10%, #2b5b84 90%)"
LOGO = "/theme/img/python-logo.png"

# Social widget
SOCIAL = (
('group', 'http://www.meetup.com/KochiPython/'), ('github', 'https://github.com/KochiPython/'), ('twitter-square', 'https://twitter.com/KochiPython'), ('facebook', 'https://www.facebook.com/groups/kochi-python'), )
# SOCIAL = (('You can add links in your config file', '#'), # ('Another social link', '#'), )

DEFAULT_PAGINATION = 10
DISQUS_SITENAME = 'kochipython'
GOOGLE_ANALYTICS = 'UA-56551965-1'
# Uncomment following line if you want document-relative URLs when developing

THEME = "themes/kochi-python"
RELATIVE_URLS = True
PLUGIN_PATHS = ['plugins']
PLUGINS = ['gravatar']