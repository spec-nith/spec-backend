PYTHON?=python3
ACTIVATE?=. .venv/bin/activate;
MANAGE=${ACTIVATE} ${PYTHON} manage.py
TEST_SETTINGS=--settings=backend.test_settings
GET_SECRET_KEY=`base64 /dev/urandom | head -c50`
ENV_FILE=.env
BLACK_ARGS=--extend-exclude="migrations|data|lib|etc|.venv" .

# Default Django Port
PORT = 8000

virtualenv:
	@echo "-> Making Virtual Environment"
	@${PYTHON} -m venv .venv

genkey: virtualenv
	@echo "-> Generating Secret key"
	@if test -f ${ENV_FILE}; then echo ".env file exists already"; true; else \
	mkdir -p $(shell dirname ${ENV_FILE}) && touch ${ENV_FILE}; \
	echo SECRET_KEY=\"${GET_SECRET_KEY}\" > ${ENV_FILE}; \
	cat etc/env.txt >> ${ENV_FILE}; fi

dev: genkey
	@echo "-> Installing Dependencies"
	@${ACTIVATE} pip3 install -r etc/dev.txt


install: genkey
	@echo "-> Installing Dependencies"
	@${ACTIVATE} pip3 install -r requirements.txt

migrate:
	${MANAGE} makemigrations
	@echo "-> Apply database migrations"
	${MANAGE} migrate

collectstatic:
	@echo "-> Collecting static files"
	${MANAGE} collectstatic

run:
	${MANAGE} runserver ${PORT}

runssl:
	${MANAGE} runsslserver ${PORT}

flush:
	@echo "-> Flushing Database"
	${MANAGE} flush

format:
	@echo "-> Run isort imports validation"
	@${ACTIVATE} isort .
	@echo "-> Run black validation"
	@${ACTIVATE} black ${BLACK_ARGS}

test:
	@${MANAGE} test ${TEST_SETTINGS}
	
check: test
	@echo "-> Run isort imports ordering validation"
	@${ACTIVATE} isort --check-only .
	@echo "-> Run black validation"
	@${ACTIVATE} black --check ${BLACK_ARGS}

coverage: 
	@echo "-> Generating coverage report"
	@${ACTIVATE} coverage erase
	@${ACTIVATE} coverage run --source='.' manage.py test ${TEST_SETTINGS}
	@${ACTIVATE} coverage report
	@${ACTIVATE} coverage html

superuser:
	@${MANAGE} createsuperuser
