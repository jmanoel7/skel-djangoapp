#!/bin/sh

# desenvolvimento
python ./manage.py runserver 0.0.0.0:8000

# producao
#python -m gunicorn --bind 0.0.0.0:8000 --workers 3 visao.wsgi:application