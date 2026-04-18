from dataclasses import dataclass
from typing import Optional


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

@dataclass
class ParsedCommand:
    action: str
    cell: Optional[str] = None
    value: Optional[str] = None
    raw: str = ""