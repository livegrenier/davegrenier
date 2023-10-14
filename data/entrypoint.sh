#!/bin/sh
echo "Waiting for postgres..."

while ! nc -z $SQL_DAVE_HOST $SQL_DAVE_PORT; do
  sleep 0.1
done

echo "PostgreSQL started"

python3 /data/manage.py makemigrations
python3 /data/manage.py migrate
python3 /data/manage.py migrate --run-syncdb

# Set the admin
python /data/manage.py createsuperuser --username=$DJANGO_USER --email=$DJANGO_EMAIL --noinput

exec "$@"

