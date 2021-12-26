@ECHO OFF
REM Setting all the environent variables for smoother experience
SET PYTHON_EXE=python
SET MANAGE=.\Scripts\python manage.py
SET ENV_FILE=.env
SET DJANGO_PORT=8000
SET AUTOFLAKE_ARGS=--in-place --remove-all-unused-imports --ignore-init-module-imports --ignore-init-module-imports -r

IF [%1]==[] (
    ECHO Please specify the function to execute
    EXIT
)
IF "%1"=="virtualenv" (
    CALL :virtualenv
)
IF "%1"=="genkey" (
    CALL :genkey
)
IF "%1"=="install" (
    CALL :virtualenv
    ECHO - Installing Dependencies
    .\Scripts\%PYTHON_EXE% -m pip install -r etc/dev.txt
	CALL :genkey
)
IF "%1"=="install_full" (
    CALL :virtualenv
    ECHO - Installing Dependencies
    .\Scripts\%PYTHON_EXE% -m pip install -r requirements.txt
    CALL :genkey
)
IF "%1"=="migrate" (
    ECHO - Migrating Database
    %MANAGE% makemigrations api
    %MANAGE% migrate
)
IF "%1"=="run" (
    ECHO - Starting Django Server
    %MANAGE% runserver %DJANGO_PORT%
)
IF "%1"=="runssl" (
    ECHO - Starting Django Server
    %MANAGE% runsslserver %DJANGO_PORT%
)
IF "%1"== "flush" (
    ECHO - Flushing Database
    %MANAGE% flush
)
IF "%1"=="format" (
	ECHO - Run isort imports ordering validation
	.\Scripts\isort --profile black api backend
	ECHO - Run black validation
	.\Scripts\black api backend
)
IF "%1"=="test" (
    ECHO - Running Unit Tests
    %MANAGE% test
)
IF "%1"=="check" (
    ECHO - Running Unit Tests
    %MANAGE% test
    ECHO - Running black validation
    .\Scripts\black --check api backend
)
IF "%1"=="coverage" (
    ECHO - Generating coverage report
    .\Scripts\coverage run --source='.' manage.py test
    .\Scripts\coverage report
    .\Scripts\coverage html
)
EXIT /B 0
:: ----------------------------------------------------------
:: Functions
:: ----------------------------------------------------------

:virtualenv
	ECHO - Making Virtual Environment
	%PYTHON_EXE% -m venv .
    EXIT /B 0

:genkey
    IF NOT EXIST .env (
        ECHO - Generating Secret key
        .\Scripts\%PYTHON_EXE% -c "from django.core.management.utils import get_random_secret_key;key = get_random_secret_key();print(f'SECRET_KEY={key}\nDEVELOPMENT=True')" -> .env
    ) ELSE (
        ECHO .env file already exists
    )
    EXIT /B 0