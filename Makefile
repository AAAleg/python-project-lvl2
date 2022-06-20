install:
		poetry install

lint:
		poetry run flake8 gendiff

run_tests:
		poetry run pytest --cov=gendiff tests/ --cov-report xml