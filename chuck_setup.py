#
# Config file for Django Chuck
#
# Setup projects by just pressing one button
#
# The following variables will be automatically injected:
# virtualenv_dir - the full path to the virtualenv
# site_dir - the full path to the projects site dir
# project_dir - combination of site_dir and site_name-project_name
# project_name - the name of the project
# site_name - the name of the site (project prefix)
#
# The following functions will be created:
# execute_in_project(cmd) - loads virtualenv and django settings and executes the given cmd
# db_cleanup - delete django tables for complete db import
# load_fixtures(file) - load the given fixture file
#

import os

project_prefix = "spr"
project_name = "sorting"
site_name = "spr-sorting"
django_settings = "sorting.settings.dev"
modules = "core,south,fabric,jquery,nginx,pil,postgres,twitter-bootstrap,uwsgi"
extra_syncdb_options = ""
extra_migrate_options = ""


def post_git_clone():
    pass


def pre_build_virtualenv():
    pass


def post_build_virtualenv():
    pass


def pre_sync_db():
    db_dir = os.path.join(site_dir, "db")

    if not os.path.exists(db_dir):
        os.makedirs(db_dir)


def post_sync_db():
    pass


def pre_migrate_db():
    pass


def post_migrate_db():
    pass
