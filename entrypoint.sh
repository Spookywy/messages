#!/bin/bash

python messages/manage.py wait_for_db
python messages/manage.py migrate --no-input
python messages/manage.py runserver 0.0.0.0:8000
