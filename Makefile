install:
		poetry install

build:
		poetry build

publish:
		poetry publish --dry-run

package-install:
		python3 -m pip install --user dist/*.whl

package-reinstall:
		python3 -m pip install --user dist/*.whl --force-reinstall

lint:
		poetry run flake8

test:
	poetry run pytest

check:
	poetry run flake8 gendiff
	poetry run pytest

gendiff:
		poetry run gendiff

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml