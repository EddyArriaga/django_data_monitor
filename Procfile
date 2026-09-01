web: python manage.py collectstatic --noinput --clear && gunicorn backend_analytics_server.wsgi:application --bind 0.0.0.0:$PORT --workers 2
