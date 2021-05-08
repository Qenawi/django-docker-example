#!/bin/sh
python3 manage.py dbrestore
python3 manage.py makemigrations myapp
python3 manage.py migrate myapp