.PHONY: help install run test lint format clean dev docs

PYTHON := python3
PIP := pip3
VENV := .venv

help:
	@echo "Neural DevOps Autopilot - Available Commands"
	@echo ""
	@echo "Development Setup:"
	@echo "  make install          Install dependencies into virtual environment"
	@echo "  make dev              Install development dependencies (includes test tools)"
	@echo ""
	@echo "Running Application:"
	@echo "  make run              Run the Streamlit application"
	@echo "  make run-port=PORT    Run on custom port (default 8501)"
	@echo ""
	@echo "Code Quality:"
	@echo "  make lint             Run code quality checks (flake8, pylint)"
	@echo "  make format           Auto-format code with black"
	@echo "  make format-check     Check code formatting without changes"
	@echo ""
	@echo "Testing:"
	@echo "  make test             Run full test suite"
	@echo "  make test-coverage    Run tests with coverage report"
	@echo ""
	@echo "Cleanup:"
	@echo "  make clean            Remove build artifacts and cache files"
	@echo "  make clean-python     Remove Python cache and .pyc files"
	@echo "  make clean-all        Remove everything including virtual environment"
	@echo ""
	@echo "Documentation:"
	@echo "  make docs             Generate project documentation"
	@echo ""

install:
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip
	$(VENV)/bin/pip install -r requirements.txt
	@echo "Installation complete. Activate with: source $(VENV)/bin/activate"

dev: install
	$(VENV)/bin/pip install pytest pytest-cov black flake8 pylint
	@echo "Development setup complete with testing and linting tools."

run:
	streamlit run app.py

run-port:
	streamlit run app.py --server.port $(port)

lint:
	@command -v flake8 >/dev/null 2>&1 || pip install flake8 pylint
	flake8 src/ app.py --max-line-length=120 --exclude=$(VENV)
	@echo "Lint check complete."

format:
	@command -v black >/dev/null 2>&1 || pip install black
	black src/ app.py --line-length=120

format-check:
	@command -v black >/dev/null 2>&1 || pip install black
	black src/ app.py --line-length=120 --check

test:
	@command -v pytest >/dev/null 2>&1 || pip install pytest
	pytest src/ -v

test-coverage:
	@command -v pytest >/dev/null 2>&1 || pip install pytest pytest-cov
	pytest src/ --cov=src --cov-report=html --cov-report=term
	@echo "Coverage report generated in htmlcov/index.html"

clean-python:
	find . -type f -name '*.py[cod]' -delete
	find . -type f -name '*$$py.class' -delete
	find . -type d -name '__pycache__' -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name '*.egg-info' -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name '.pytest_cache' -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name '.mypy_cache' -exec rm -rf {} + 2>/dev/null || true

clean: clean-python
	rm -rf build/ dist/ htmlcov/
	rm -f .coverage
	find . -type f -name '.DS_Store' -delete

clean-all: clean
	rm -rf $(VENV)
	@echo "Virtual environment removed. To reinstall, run: make install"

docs:
	@echo "Documentation generation placeholder."
	@echo "Add documentation generation tools as needed (sphinx, pdoc, etc.)"

.DEFAULT_GOAL := help
