# -*- coding: utf-8 -*-

import os, sys
from sorting.settings.custom import *  # @UnusedWildImport

ugettext = lambda s: s

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.dirname(PROJECT_ROOT)

sys.path.append(SITE_ROOT) # TODO Is this really necessary (i.e. production server)?
sys.path.append(PROJECT_ROOT)
sys.path.append(PROJECT_ROOT + '/apps/')
sys.path.append(PROJECT_ROOT + '/libs/')


# Generazione automatica SECRET_KEY
def generate_secret_key(file_path):
	from django.utils.crypto import get_random_string
	chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
	secret_key = get_random_string(50, chars)
	with open(file_path, "w") as text_file:
		text_file.write("SECRET_KEY = '%s'" % secret_key)
try:
    from secret_key import *
except ImportError:
    SETTINGS_DIR = os.path.abspath(os.path.dirname(__file__))
    generate_secret_key(os.path.join(SETTINGS_DIR, 'secret_key.py'))
    from secret_key import *

# Invio email con classe send_mail configurata con smtp google
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'sendmail@cambieri.it'
# EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_SUBJECT_PREFIX = '[Django - sorting] '


DEBUG = True
TEMPLATE_DEBUG = DEBUG

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

APPEND_SLASH = True

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True


# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(SITE_ROOT, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
        os.path.join(PROJECT_ROOT, 'static'),
    )

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    )

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin/'


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
    )


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    )


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.media',
    'django.core.context_processors.debug',
    )


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    )

ROOT_URLCONF = 'sorting.urls'

TEMPLATE_DIRS = (
        os.path.join(PROJECT_ROOT, 'templates'),
    )

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    
    # Le apps del progetto vanno messe prima di 'admin' per poter personalizzare i messaggi in 'locale'
    'main',
    'django.contrib.admin',
    'south',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Save timestamps in utc
# USE_TZ = True

# cickhacking protection
X_FRAME_OPTIONS = 'DENY'

BASE_OFFSET_X = 50
BASE_OFFSET_Y = 50

INC_X = 10
INC_Y = 10
INC_REPEAT_DELAY = 50 # millisecondi (più basso = più veloce)

LEFT_WING_OFFSET = -300
RIGHT_WING_OFFSET = 300

SUCTION_CUPS = (
	(1,		0,		0, 		40, 	40, 	'left'),
	(2, 	230, 	0, 		40, 	40, 	'left'),
	(3, 	450, 	0, 		40, 	40, 	'left'),
	(4, 	670, 	0, 		40, 	40, 	'left'),
	(5, 	0, 		130, 	40, 	40, 	'left'),
	(6, 	230, 	130, 	40, 	40, 	'left'),
	(7, 	450, 	130, 	40, 	40, 	'left'),
	(8, 	670, 	130, 	40, 	40, 	'left'),
	(9, 	1070, 	0, 		40, 	40, 	'right'),
	(10, 	1290, 	0, 		40, 	40, 	'right'),
	(11, 	1510, 	0, 		40, 	40, 	'right'),
	(12, 	1740, 	0, 		40, 	40, 	'right'),
	(13, 	1070,	130, 	40, 	40, 	'right'),
	(14, 	1290, 	130, 	40, 	40, 	'right'),
	(15, 	1510, 	130, 	40, 	40, 	'right'),
	(16, 	1740, 	130, 	40, 	40, 	'right'),
	(17, 	200, 	230, 	40, 	40, 	'left'),
	(18,	0, 		360, 	40, 	40, 	'left'),
	(19, 	230, 	360, 	40, 	40, 	'left'),
	(20, 	450, 	360, 	40, 	40, 	'left'),
	(21, 	670, 	360, 	40, 	40, 	'left'),
	(22,	0, 		490, 	40, 	40, 	'left'),
	(23, 	230, 	490, 	40, 	40, 	'left'),
	(24, 	450, 	490, 	40, 	40, 	'left'),
	(25, 	670, 	490, 	40, 	40, 	'left'),
	(26, 	200, 	620, 	40, 	40, 	'left'),
	(27, 	1270, 	230, 	40, 	40, 	'right'),
	(28,	1070, 	360, 	40, 	40, 	'right'),
	(29, 	1300, 	360, 	40, 	40, 	'right'),
	(30, 	1520, 	360, 	40, 	40, 	'right'),
	(31, 	1740, 	360, 	40, 	40, 	'right'),
	(32,	1070, 	490, 	40, 	40, 	'right'),
	(33, 	1300, 	490, 	40, 	40, 	'right'),
	(34, 	1520, 	490, 	40, 	40, 	'right'),
	(35, 	1740, 	490, 	40, 	40, 	'right'),
	(36, 	1270, 	620, 	40, 	40, 	'right'),
	(37,	0,		720, 	40, 	40, 	'left'),
	(38, 	230, 	720, 	40, 	40, 	'left'),
	(39, 	450, 	720, 	40, 	40, 	'left'),
	(40, 	670, 	720, 	40, 	40, 	'left'),
	(41, 	0, 		850, 	40, 	40, 	'left'),
	(42, 	230, 	850, 	40, 	40, 	'left'),
	(43, 	450, 	850, 	40, 	40, 	'left'),
	(44, 	670, 	850, 	40, 	40, 	'left'),
	(45,	1070,	720, 	40, 	40, 	'right'),
	(46, 	1290, 	720, 	40, 	40, 	'right'),
	(47, 	1510, 	720, 	40, 	40, 	'right'),
	(48, 	1740, 	720, 	40, 	40, 	'right'),
	(49, 	1070,	850, 	40, 	40, 	'right'),
	(50, 	1290, 	850, 	40, 	40, 	'right'),
	(51, 	1510, 	850, 	40, 	40, 	'right'),
	(52, 	1740, 	850, 	40, 	40, 	'right'),			
)

SOCKET_DATA = {
			 'myip' : ''
			,'myport' : 2000
			,'otherip' : '192.168.99.1'
			,'otherport' : 2000
			,'bytestx' : 66
			,'bytesrx' : 16
			,'dimensionfactor' : 1
			,'folder' : 'ima'
			,'file' : 'pos_01.ini'
}


