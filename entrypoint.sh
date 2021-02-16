#!/bin/sh
cd stock
python manage.py createsuperuser admin
python manage.py makemigrations
python manage.py migrate
python manage,py runserver 0.0.0.0:8000


