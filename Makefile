.PHONY: bootstrap governance lint test build security security-node security-python ci precommit-install precommit-run dev-api dev-worker clean

bootstrap:
	cd apps/control-plane && npm ci
	cd apps/worker && uv sync

governance:
	python3 project_management/scripts/validate_sprint_governance.py

lint:
	cd apps/control-plane && npm run lint
	cd apps/worker && uv run ruff check .

test:
	cd apps/control-plane && npm test
	cd apps/worker && uv run python -m pytest -q

build:
	cd apps/control-plane && npm run build

security: security-node security-python

security-node:
	cd apps/control-plane && npm audit --omit=dev --audit-level=high

security-python:
	cd apps/worker && tmp=$$(mktemp) && uv export --format requirements-txt --no-hashes > $$tmp && uv run pip-audit -r $$tmp && rm -f $$tmp
	cd apps/worker && uv run bandit -q -r worker -ll -ii

ci: governance lint test build security

precommit-install:
	uvx pre-commit install --hook-type pre-commit --hook-type pre-push

precommit-run:
	uvx pre-commit run --all-files

dev-api:
	cd apps/control-plane && npm run dev

dev-worker:
	cd apps/worker && uv run python -m worker

clean:
	rm -rf apps/control-plane/node_modules apps/control-plane/dist apps/control-plane/.turbo
	rm -rf apps/worker/.venv apps/worker/.pytest_cache apps/worker/.ruff_cache apps/worker/__pycache__
	rm -rf data
