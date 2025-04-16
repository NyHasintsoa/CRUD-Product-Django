# Variables
DJANGO_ADMIN = django-admin
PYTHON = python3
PYTHON_MANAGE = $(PYTHON) manage.py
PORT = 8000
PARAMS := $(wordlist 2, $(words $(MAKECMDGOALS)), $(MAKECMDGOALS))


# Django-admin
.PHONY: startproject
startproject: ## Create the project
	$(DJANGO_ADMIN) startproject $(PARAMS)

.PHONY: startapp
startapp: ## Create an app for the our project
	$(PYTHON_MANAGE) startapp $(PARAMS)
	
.PHONY: app
app: ## Alias startapp
	$(MAKE) startapp $(PARAMS)

.PHONY: test
test: ## Run the test of our project
	$(PYTHON_MANAGE) test

# Server
.PHONY: runserver
runserver: ## Create a local server
	$(PYTHON_MANAGE) runserver $(PORT)

.PHONY: serve
serve: ## Alias runserver
	$(MAKE) runserver

# Database
.PHONY: makemigrations
makemigrations: ## Create an command who migrate to database
	$(PYTHON_MANAGE) makemigrations

.PHONY: migrations
migrations: ## Alias makemigrations
	$(MAKE) makemigrations

.PHONY: migrate
migrate: ## Migrate all the entity to the database
	$(PYTHON_MANAGE) migrate

# User (auth)
.PHONY: createsuperuser
createsuperuser: ## create an user who have an access to all commands
	$(PYTHON_MANAGE) createsuperuser

.PHONY: superuser
superuser: ## Alias createsuperuser
	$(MAKE) createsuperuser

.PHONY: changepassword
changepassword: ## change password of the user
	$(PYTHON_MANAGE) changepassword

.PHONY: djangohelp
djangohelp: ## help for django
	$(PYTHON_MANAGE) help

# help
.PHONY: help
help: ## All command line
	@grep -E '(^[a-zA-Z_-]+:.*?##.*$$)|(^##)' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' | sed -e 's/\[32m##/[33m/'
