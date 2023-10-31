lint:
	mypy . --explicit-package-bases
	isort .
	flake8 .
	black .