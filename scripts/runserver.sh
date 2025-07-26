#!/bin/sh
python -m gunicorn --bind 0.0.0.0:8000 --workers 3 project.wsgi:application
