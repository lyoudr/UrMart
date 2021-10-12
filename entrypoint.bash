#!/bin/bash

echo "Collect Static Files"
python3 manage.py collectstatic --noinput

echo "Apply Database Migrations"
python3 manage.py migrate

echo "Load default data"
python3 manage.py loaddata_cus ./*/fixtures/*.yaml

echo "Start Redis server"
service redis-server start

echo "Test Redis server status"
redis-cli ping

echo "Start periodic task which count shop info"
celery -A product beat -l INFO --logfile=log/celery.beat.log --detach

echo "Start worker for consuming tasks stored in Queue Queue default"
celery -A product worker --concurrency=1 -l INFO -Q default --logfile=log/celery.log --detach

echo "Start the Django server"
# localhost => 0.0.0.0:5000
# python3 manage.py runserver 0.0.0.0:$PORT

# heroku => 0.0.0.0:$PORT
uwsgi --ini uwsgi.ini