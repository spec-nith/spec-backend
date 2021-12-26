PYTHON_EXE?=python3
MANAGE=bin/python manage.py
ACTIVATE?=. bin/activate;
GET_SECRET_KEY=`base64 /dev/urandom | head -c50`
ENV_FILE=.env
AUTOFLAKE_ARGS=--in-place --remove-all-unused-imports --ignore-init-module-imports --ignore-init-module-imports -r

# Default Django Port
PORT = 8000

virtualenv:
	@echo "-> Getting Essential Build Files"
	@sudo apt-get install python3-venv
	@echo "-> Making Virtual Environment"
	@${PYTHON_EXE} -m venv .

genkey: virtualenv
	@echo "-> Generating Secret key"
	@if test -f ${ENV_FILE}; then echo ".env file exists already"; true; fi
	@mkdir -p $(shell dirname ${ENV_FILE}) && touch ${ENV_FILE}
	@echo SECRET_KEY=\"${GET_SECRET_KEY}\"\\nDEVELOPMENT=True > ${ENV_FILE}

install: genkey
	@echo "-> Installing Dependencies"
	@${ACTIVATE} pip install -r etc/dev.txt


install_full: genkey
	@echo "-> Installing Dependencies"
	@${ACTIVATE} pip install -r requirements.txt

migrate:
	@echo "-> Apply database migrations"
	${MANAGE} makemigrations api
	${MANAGE} migrate

run:
	${MANAGE} runserver ${PORT}

runssl:
	${MANAGE} runsslserver ${PORT}

flush:
	@echo "-> Flushing Database"
	${MANAGE} flush

format:
	@echo "-> Run isort imports ordering validation"
	@${ACTIVATE} isort api backend
	@echo "-> Run black validation"
	@${ACTIVATE} black api backend

test:
	@${MANAGE} test

check: test
	@echo "-> Run black validation"
	@${ACTIVATE} black --check api backend

coverage: 
	@echo "-> Generating coverage report"
	@${ACTIVATE} coverage run --source='.' manage.py test
	@${ACTIVATE} coverage report
	@${ACTIVATE} coverage html