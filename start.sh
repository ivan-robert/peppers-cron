#!/bin/bash

# Run database migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

# Setup scheduled tasks
python manage.py setup_schedule

# Start gunicorn server (WEB SERVICE ONLY)
gunicorn app.wsgi:application --bind 0.0.0.0:$PORT