#!/bin/sh

set -e

python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py migrate

daphne -b 0.0.0.0 -p 8001 messages.asgi:application
