#! /bin/bash

python manage.py migrate --no-input

exec gunicorn news_board.wsgi:application -b 0.0.0.0:8000 --reload
