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
		poetry run flake8 gendiff

test:
	poetry run pytest

check:
	poetry run flake8 gen_diff
	poetry run pytest

gendiff:
		poetry run gendiff