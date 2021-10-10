#!/bin/bash

echo "Collect Static Files"
python3 manage.py collectstatic --noinput

echo "Apply Database Migrations"
python3 manage.py migrate

echo "Load default data"
python3 manage.py loaddata_cus ./*/fixtures/*.yaml

echo "start periodic task which count shop info"
celery -A product beat -l INFO --logfile=log/celery.beat.log --detach

echo "start worker for consuming tasks stored in Queue Queue default"
celery -A product worker --concurrency=1 -l INFO -Q default --logfile=log/celery.log --detach

echo "Start the Django server"
python3 manage.py runserver 0.0.0.0:5000