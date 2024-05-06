FILE_JSON = json_file/file3.json json_file/file4.json
FILE_YML = json_file/file1.yml json_file/file2.yml
.PHONY: install build tests lint gendiff_json gendiff_yml

install:
	poetry install

build:
	poetry build

tests:
	python -m pytest tests

lint:
	poetry run flake8 gendiff

test-coverage:
    poetry run pytest --cov=gendiff --cov-report xml

gendiff_json:
	poetry run gendiff $(FILE_JSON)
	
gendiff_yml:
	poetry run gendiff $(FILE_YML)
