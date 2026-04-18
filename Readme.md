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
├── Readme.md
├── app/
│   ├── controller.py
│   ├── game.py
│   ├── generator.py
│   ├── parser.py
│   ├── render.py
│   ├── validation.py
│   ├── models.py
│   └── constants.py
└── test/
    ├── test_game.py
    ├── test_generator.py
    ├── test_parser.py
    └── test_validation.py
```

# Design overview

The codebase is organised using a modular layered design with clear separation of concerns:

- `main.py` – application entry point and game loop
- `controller.py` – routes parsed commands to the correct actions
- `parser.py` – parses user input commands such as `A3 4`, `hint`, `check`
- `game.py` – gameplay operations such as insert, remove, and hint
- `validation.py` – validates Sudoku rules, board completion, and user moves
- `generator.py` – dynamically generates a new Sudoku puzzle for each game
- `render.py` – prints the Sudoku board to the terminal
- `models.py` – shared dataclasses / models

Assumption - Hint function will only provide the next hint if the board is already valid

# Requirements for this project

```text
Python 3.11 or later
pytest
```

# Installation

## For Mac users

```bash
# Clone the repository
git clone https://github.com/Ronith900/sudoku.git

# Move into project folder
cd sudoku

# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## For Windows users

```bash
# Clone the repository
git clone https://github.com/Ronith900/sudoku.git

# Move into project folder
cd sudoku

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

# To run the game

```bash
From the Project root
python main.py
```

# To execute the test cases

```bash
From the Project root
python -m pytest -v
```

# Demo

### Start Game

<img src="screenshots/game_start.png" width="700">

### Clear and Hint Feature

<img src="screenshots/clear_hint.png" width="700">

### Pytest Results

<img src="screenshots/test_cases_results.png" width="700">

### User Input

<img src="screenshots/user_input.png" width="700">
