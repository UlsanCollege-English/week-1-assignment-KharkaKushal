# Week 1 Assignment — Python Challenges

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/qF8WcF0i)
[![Autograding Tests](https://github.com/UlsanCollege-English/week-1-assignment-KharkaKushal/actions/workflows/classroom.yml/badge.svg)](https://github.com/UlsanCollege-English/week-1-assignment-KharkaKushal/actions/workflows/classroom.yml)

A collection of foundational Python functions covering arithmetic, parity checking, linear search, counting, and reverse indexing.

## Features

- **`add(a, b)`** — Returns the sum of two integers.
- **`is_even(n)`** — Checks whether an integer is even.
- **`linear_search(nums, target)`** — Finds the first occurrence of a target in a sequence.
- **`count_occurrences(items, target)`** — Counts how many times a target appears.
- **`last_index(nums, target)`** — Finds the last occurrence of a target in a sequence.

## Tech Stack

- **Python** 3.13+
- **pytest** 9.0+ for testing

## Quick Start

```bash
# Clone the repository
git clone https://github.com/UlsanCollege-English/week-1-assignment-KharkaKushal.git
cd week-1-assignment-KharkaKushal

# (Optional) Create a virtual environment
python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate  # macOS / Linux

# Install dependencies
pip install pytest

# Run tests
pytest
```

## Project Structure

```
week-1-assignment-KharkaKushal/
├── .github/workflows/    # CI / autograding workflow
├── docs/                 # Documentation
├── src/
│   ├── __init__.py
│   └── challenges.py     # Function implementations
├── tests/
│   └── test_challenges.py # pytest test suite
├── .gitignore
└── README.md
```

## Development

All functions are in `src/challenges.py`. Add new tests in `tests/test_challenges.py`. Run the test suite with:

```bash
pytest -v
```

## License

This project is part of a Ulsan College English course assignment.
