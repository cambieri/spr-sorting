source /home/workspace-django/virtualenvs/spr-sorting/bin/activate
cd /home/workspace-django/projects/spr-sorting/sorting/
fab live prepare_deploy
fab live deploy
deactivate
