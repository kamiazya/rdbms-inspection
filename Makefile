.PHONY: lint format test

TARGET = .

lint:
	poetry run mypy $(TARGET)
	poetry run flake8 --show-source $(TARGET)
	poetry run poetry run black $(TARGET) --check
	poetry run isort --force-single-line-imports --check $(TARGET)


format:
	poetry run autopep8 -ivr $(TARGET)
	poetry run black $(TARGET)
	poetry run isort --force-single-line-imports $(TARGET)

test:
	PYTHONPATH=./$(TARGET) poetry run pytest
