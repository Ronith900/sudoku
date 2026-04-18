# Sudoku Command Line Game

A Python command-line Sudoku game that allows users to play Sudoku in the terminal.

Features include:

- Play Sudoku using simple text commands
- Insert numbers into cells
- Clear user-entered cells
- Validate board rules
- Get hints
- Detect puzzle completion
- Automated tests using pytest

---

# Project Structure

```text
sudoku/
├── main.py
├── game.py
├── parser.py
├── render.py
├── models.py
├── constants.py
├── README.md
└── tests/
    ├── test_game.py
    └── test_parser.py
```

# Requirements for this project

```text
Python 3.12 (or your version)
pytest
```

## Installation

```bash
git clone https://github.com/Ronith900/sudoku.git
cd sudoku

For Mac users
    python -m venv venv (Create venv)
    source venv/bin/activate

pip install -r requirements.txt
```

# How to run the game

```bash
From the Project root
python main.py
```
