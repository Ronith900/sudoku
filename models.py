from dataclasses import dataclass


@dataclass
class UserInput:
    cell: str
    value: str


@dataclass
class SudokuCheckReport:
    valid: bool
    verdict: str


@dataclass
class HintReport:
    board_valid: bool
    board_filled: bool
    message: str