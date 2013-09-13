# -*- coding: utf-8 -*-
# These settings are valid for:
# - sites: all
# - environments: prod

import os
from sorting.settings.common import *

# Debugging
DEBUG = False
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['sorting.cambieri.info', 'www.cambieri.info', 'cambieri.info', 'cmbhosting.no-ip.biz', '89.32.146.242']

# Misc
PREPEND_WWW = False

# Cache
CACHES = {
        'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
    }

# Database
DATABASES = {
    #    'default': {
#    	'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#    	'NAME': os.path.join(SITE_ROOT, 'db','dev.sqlite3'), # Or path to database file if using sqlite3.
#    	'USER': '', # Not used with sqlite3.
#    	'PASSWORD': '', # Not used with sqlite3.
#    	'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
#    	'PORT': '', # Set to empty string for default. Not used with sqlite3.
#    },
    
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'spr_sorting_live',                      # Or path to database file if using sqlite3.
        'USER': 'spr_sorting_live',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    },
}

DEFAULT_CHARSET='utf-8'


