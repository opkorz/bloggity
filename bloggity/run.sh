#!/bin/bash
if [ "$BLOGGITY_ENV" = "DEV" ]; then
  python manage.py runserver
else
  gunicorn \
    -c gunicorn.conf.py \
    wsgi:app
fi