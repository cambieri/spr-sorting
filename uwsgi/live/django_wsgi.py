import os
import django.core.handlers.wsgi

os.environ['DJANGO_SETTINGS_MODULE'] = 'sorting.settings.live'
application = django.core.handlers.wsgi.WSGIHandler()
