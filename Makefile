.PHONY: install build tests lint gendiff_json gendiff_yml

install:
	poetry install

build:
	poetry build

tests:
	poetry run pytest tests -vv

lint:
	poetry run flake8 gendiff

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
