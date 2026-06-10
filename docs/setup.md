# Setup Guide

## Prerequisites

- Python 3.13 or later
- pip package manager
- Git

## Installation

```bash
# Clone the repository
git clone https://github.com/UlsanCollege-English/week-1-assignment-KharkaKushal.git
cd week-1-assignment-KharkaKushal

# Create virtual environment (recommended)
python -m venv .venv

# Activate it
# Windows:
.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate

# Install pytest
pip install pytest

# Verify setup
pytest --version
```

## Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run a specific test file
pytest tests/test_challenges.py

# Run a specific test
pytest tests/test_challenges.py::test_add_basic
```
