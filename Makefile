install:
	poetry install

package-install:
	python3 -m pip install --user dist/*.whl

build:
	poetry build

publish:
	poetry publish --dry-run

gendiff:
	poetry run gendiff

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov
