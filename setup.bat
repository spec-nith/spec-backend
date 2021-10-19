@echo off
set PYTHON_EXE="python3"
set MANAGE="python3 ./manage.py"
set ENV_FILE=".env"
set DJANGO_PORT="8000"

python -m venv .
type nul > .env
python -c "from django.core.management.utils import get_random_secret_key;key = get_random_secret_key;print(f'SECRET_KEY={key}')" > .env
.\Scripts\pip install -r etc/dev.txt