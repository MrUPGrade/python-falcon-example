SHELL=/bin/bash
PIP_INSTALL:=pip install --upgrade

E:= source dev-env.sh;

DC:=docker-compose

DCE:=$(E) $(DC) -p pft -f docker-compose.yaml
DCE_TEST:=$(DCE) -f docker-compose-test.yaml

DOCKER:=docker

export PYTHONPATH:=$(shell pwd)



pip-install:
	$(PIP_INSTALL) pip
	$(PIP_INSTALL) setuptools
	$(PIP_INSTALL) -r requirements.txt
	$(PIP_INSTALL) -r requirements-dev.txt



docker-build:
	$(DOCKER) build -t pft:dev .



test:
	$(E) pytest --cov=pft

test-html:
	$(E) pytest --cov=pft --cov-report html:artifacts/cov



env-dev-up:
	$(DCE) up -d
	sleep 5
	$(E) python pft/cli.py initdb

env-dev-down:
	-$(DCE) down

env-dev-setup: env-dev-down env-dev-up

env-dev-logs:
	$(DCE) logs -f

env-dev-app-run: docker-build
	$(DOCKER) run --rm -it --env-file .env -u 1000 -p 10080:8080 pft:dev



env-test-up:
	$(DCE_TEST) up --build -d

env-test-down:
	-$(DCE_TEST) down

env-test-setup: env-test-down env-test-up

env-test-logs:
	$(DCE_TEST) logs -f

env-test-cmd:
	@echo $(DC) -p pft -f docker-compose.yaml -f docker-compose-test.yaml
