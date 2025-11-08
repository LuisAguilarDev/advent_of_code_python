
# 🎄 Advent of Code Python Solutions

Welcome! This repository contains my solutions for [Advent of Code](https://adventofcode.com/) puzzles, written in Python.

---

## 🚀 Zero-Setup: Just Open in Dev Container

**No installation required!**

Simply open this project in a [Dev Container](https://containers.dev/) (like GitHub Codespaces or VS Code Remote Containers).

You get a **100% safe, isolated environment** with all dependencies pre-installed:

- Python 3 (with pip)
- Git (latest)
- All tools on the `PATH`

Your local system is never changed. Everything runs inside a disposable, secure container.

---

## 📁 Project Structure

```
advent_of_code_python/
├── src/
│   ├── 2023/
│   │   └── day3/
│   │       ├── index.py
│   │       ├── input.txt
│   │       └── sample.txt
│   └── constants/
│       └── constants.py
├── README.md
└── ...
```

---

## ▶️ How to Run

1. **Open this repo in your Dev Container.**
2. **Open a terminal in VS Code.**
3. **Run the solution as a module:**

   **From the repository root:**
   ```sh
   python -m src.2023.day1.index
   ```

   **Or from the src directory:**
   ```sh
   cd src
   python -m 2023.day1.index
   ```

> **Note:**
> Running as a module ensures all imports work correctly! Use dots (.) to separate path components, not slashes (/), and omit the .py extension.

### 🧪 Running Tests

**Run all tests:**
```sh
pytest -q
```

**Run tests for a specific day:**
```sh
pytest -q test/2023/day1/test_day1.py
```

**Run tests with verbose output:**
```sh
pytest -v
```

**Run tests and show coverage:**
```sh
pytest --cov=src --cov-report=term-missing
```

> **Note:** Empty `__init__.py` files are automatically excluded from coverage reports. Files with actual code (like `src/global_utils/__init__.py`) are included as they contain testable logic.

---

## 🛡️ Safe & Private

- Runs in a closed, disposable container
- No changes to your local system
- All tools are pre-installed and ready to use

---

## 🧭 Features

- Modular, year/day-based structure
- Reusable constants for grid puzzles
- Ready for extension and testing

---

## 📚 Resources

- [Advent of Code](https://adventofcode.com/)
- [Python Documentation](https://docs.python.org/3/)

---

Happy coding and puzzle solving! 🎅✨

# Best Practices for Solving Puzzles

Below are short, practical explanations for the coding practices. Apply these consistently to make solutions easier to read, debug, test and maintain. use type hinting following these practices will be easier for u return in a few months and understand what did u do on ur last journey!.

## 1) Debuggable code
- Use the `logger` function imported from utils instead of naked `print()` calls so you can control verbosity.
- Keep functions small and single-purpose — easier to step through and unit test.
- Add meaningful variable names and short docstrings; include examples in docstrings for tricky behaviour.
- Add reproducible examples / sample inputs in the repository so you can run the failing case locally.

Example:
```python
# ...existing code...
from utils.logger import logger

def solve(lines: list[str]) -> int:
    """Solve one puzzle. Returns result as integer."""
    logger.debug("starting solve with %d lines", len(lines))
    # ...
# ...existing code...
```

## 2) Proper abstractions
- Group domain logic into well-named functions and small classes; separate parsing, business logic and I/O.
- Keep file I/O and parsing in utilities (`utils.read_file`) and pure functions for the algorithm itself (take and return plain data structures).
- Prefer composable building blocks over very long monolithic functions.
- Encapsulate mutability: return new data instead of mutating global state where possible.

Example structure:
- parse_input(...) -> returns structured data
- compute_part1(data) -> returns result
- compute_part2(data) -> returns result
- main() -> reads files, calls functions, prints results

## 3) Unit testing
- Use pytest and keep tests small and deterministic. Put tests under `test/` mirroring the `src/` layout.
- Test edge cases, typical cases and the provided samples from the puzzle.
- Use `test_utils.load_module` to dynamically load and test modules from `src/`.
- Run tests automatically in CI (or locally via `pytest`).

Test example:
```python
# test/2023/day1/test_day1.py
from test_utils import load_module
from global_utils.utils import read_file

module = load_module("src/2023/day1")

def test_find_number_examples():
    assert module.find_number("1abc2") == 12
    assert module.find_number("pqr3stu8vwx") == 38
    assert module.find_number("a1b2c3d4e5f") == 15
    assert module.find_number("treb7uchet") == 77

def test_sum_calibration_examples():
    lines = read_file("test/2023/day1/sample1.txt")
    assert module.sum_calibration(lines) == 142

def test_part1_input_answer():
    lines = read_file("src/2023/day1/input.txt")
    assert module.sum_calibration(lines) == 54573
```

## 4) Error handling
- Validate inputs early and raise clear, specific exceptions (custom exceptions for domain errors if helpful).
- Catch only expected exceptions and re-raise with context when needed; avoid broad `except:`.
- Use context managers for resource handling (`with open(...) as f:`).
- Provide helpful error messages showing tried paths or inputs (useful in `utils.read_file`).

Example:
```python
if not lines:
    raise ValueError("input file is empty; expected at least one line")
```

---

Apply these patterns while solving each puzzle: keep the I/O thin, the algorithm pure and small, add tests for the algorithm, and prefer logged, configurable debug output. This makes it far easier to reproduce, debug and maintain solutions.