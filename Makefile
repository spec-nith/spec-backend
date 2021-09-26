PYTHON_EXE?=python3
MANAGE=bin/python manage.py
ACTIVATE?=. bin/activate;
GET_SECRET_KEY=`base64 /dev/urandom | head -c50`
ENV_FILE=.env

# Default Django Port
PORT = 8000

virtualenv:
	@echo "-> Making Virtual Environment"
	@${PYTHON_EXE} -m venv .

install: virtualenv
	@echo "-> Generating Secret key"
	@if test -f ${ENV_FILE}; then echo ".env file exists already"; true; fi
	@mkdir -p $(shell dirname ${ENV_FILE}) && touch ${ENV_FILE}
	@echo SECRET_KEY=\"${GET_SECRET_KEY}\" > ${ENV_FILE}
	@echo "-> Installing Dependencies"
	@${ACTIVATE} pip install -r requirements.txt

migrate:
	@echo "-> Apply database migrations"
	${MANAGE} makemigrations
	${MANAGE} migrate

run:
	${MANAGE} runserver ${PORT}

freeze:
	@echo "-> Updating Project Requirements"
	@${ACTIVATE} pip freeze > requirements.txt

flush:
	@echo "-> Flushing Database"
	${MANAGE} flush

format:
	@echo "-> Run isort imports ordering validation"
	@isort --gitignore .
	@echo "-> Run black validation"
	@black .

test:
	@${MANAGE} test

check:
	@echo "-> Run black validation"
	@${ACTIVATE} black --check .