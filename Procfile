web: gunicorn backend.wsgi --log-file -
release: python3 manage.py makemigrations api
release: python3 manage.py makemigrations
release: python3 manage.py migrate