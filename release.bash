#!/bin/bash

echo "Start Redis server"
redis-server --daemonize yes

echo "Test Redis server status"
redis-cli ping

echo "Start periodic task which count shop info"
celery -A product beat -l INFO --logfile=log/celery.beat.log --detach

echo "Start worker for consuming tasks stored in Queue Queue default"
celery -A product worker --concurrency=1 -l INFO -Q default --logfile=log/celery.log --detach