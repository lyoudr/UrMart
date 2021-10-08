# echo "start periodic task which sync erp oracle db and local postgres db"
celery -A product beat -l INFO --logfile=celery.beat.log --detach

# echo "start worker for consuming tasks stored in Queue erp_tables and Queue default"
celery -A product worker --concurrency=1 -l INFO -Q default --logfile=celery.log