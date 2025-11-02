start:
	./.venv/bin/python3 app.py

requirements:
	./.venv/bin/pip freeze > requirements.txt

environment:
	python3 -m venv ./.venv