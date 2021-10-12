#!/bin/bash

echo "Collect Static Files"
python3 manage.py collectstatic --noinput

echo "Apply Database Migrations"
python3 manage.py migrate

echo "Load default data"
python3 manage.py loaddata_cus ./*/fixtures/*.yaml

echo "Start the Django server"
# localhost => 0.0.0.0:5000
# python3 manage.py runserver 0.0.0.0:$PORT

# heroku => 0.0.0.0:$PORT
uwsgi --ini uwsgi.ini