SHELL:=/usr/bin/env bash

.PHONY: lint
lint:
	poetry run ruff check --exit-non-zero-on-fix
	poetry run ruff format --check
	poetry run flake8 .
	poetry run mypy .

.PHONY: package
package:
	poetry check
	poetry run pip check

.PHONY: smoke
smoke:
	poetry run pygmentize -f rtf -P style=pustota pustota_pygments/__init__.py > /dev/null
	poetry run pygmentize -f rtf -P style=pustota-light pustota_pygments/__init__.py > /dev/null

.PHONY: test
test: smoke lint package
