from collections import defaultdict
from typing import Optional

from constants import ROW_MAPPING, INDEX_TO_ROW, PUZZLE
from models import UserInput, SudokuCheckReport, HintReport


def get_pre_filled_cells():
    pre_filled_cells = set()

    for row_index in range(len(PUZZLE)):
        for col_index in range(len(PUZZLE[row_index])):
            if PUZZLE[row_index][col_index] != ".":
                pre_filled_cells.add(f"{INDEX_TO_ROW[row_index]}{col_index + 1}")

    return pre_filled_cells


def get_user_object_from_user_response(user_response: str) -> UserInput:
    cell, value = user_response.split(" ")
    return UserInput(cell, value)


def is_user_input_cell_valid(user_input: UserInput) -> bool:
    pre_filled_cells = get_pre_filled_cells()
    return user_input.cell not in pre_filled_cells


def is_user_input_value_valid(user_input: UserInput) -> bool:
    try:
        input_int = int(user_input.value)
        return 1 <= input_int <= 9
    except ValueError:
        return False


def is_sudoku_grid_valid(board) -> SudokuCheckReport:
    rows = defaultdict(set)
    cols = defaultdict(set)
    grids = defaultdict(set)

    for row_index in range(len(board)):
        for col_index in range(len(board[row_index])):
            current_value = board[row_index][col_index]

            if current_value == ".":
                continue

            if current_value in rows[row_index]:
                return SudokuCheckReport(
                    False,
                    f"Number {current_value} already exists in row {INDEX_TO_ROW[row_index]}",
                )

            if current_value in grids[(row_index // 3, col_index // 3)]:
                return SudokuCheckReport(
                    False,
                    f"Number {current_value} already exists in 3*3 grid",
                )

            if current_value in cols[col_index]:
                return SudokuCheckReport(
                    False,
                    f"Number {current_value} already exists in column {col_index + 1}",
                )

            rows[row_index].add(current_value)
            cols[col_index].add(current_value)
            grids[(row_index // 3, col_index // 3)].add(current_value)

    return SudokuCheckReport(True, "No rule violations detected.")


def insert_user_input(user_input: UserInput, board):
    row = ROW_MAPPING[user_input.cell[0]]
    col = int(user_input.cell[1]) - 1

    if board[row][col] == ".":
        board[row][col] = user_input.value

    return board


def remove_user_input(user_input: UserInput, board):
    row = ROW_MAPPING[user_input.cell[0]]
    col = int(user_input.cell[1]) - 1
    board[row][col] = "."
    return board


def is_sudoku_board_filled(board):
    required = len(board) * len(board[0])
    filled = 0

    for row in board:
        for value in row:
            if value != ".":
                filled += 1

    return required == filled


def game_is_completed(board):
    board_valid = is_sudoku_grid_valid(board)
    values_filled = is_sudoku_board_filled(board)
    return board_valid.valid and values_filled


def get_candidates(board, row, col):
    if board[row][col] != ".":
        return set()

    digits = set("123456789")
    existing_row_values = {board[row][c] for c in range(9) if board[row][c] != "."}
    existing_col_values = {board[r][col] for r in range(9) if board[r][col] != "."}
    existing_grid_values = {
        board[r][c]
        for r in range((row // 3) * 3, (row // 3) * 3 + 3)
        for c in range((col // 3) * 3, (col // 3) * 3 + 3)
        if board[r][c] != "."
    }

    return digits - (existing_row_values | existing_col_values | existing_grid_values)


def hint(board) -> HintReport:
    if not is_sudoku_grid_valid(board).valid:
        return HintReport(
            board_valid=False,
            board_filled=False,
            message="Board is Invalid",
        )

    if is_sudoku_board_filled(board):
        return HintReport(
            board_valid=True,
            board_filled=True,
            message="Board is already complete",
        )

    for row_index in range(len(board)):
        for col_index in range(len(board[row_index])):
            if board[row_index][col_index] == ".":
                candidates = get_candidates(board, row_index, col_index)
                if len(candidates) == 1:
                    value = next(iter(candidates))
                    return HintReport(
                        board_valid=True,
                        board_filled=False,
                        message=f"Hint cell: {INDEX_TO_ROW[row_index]}{col_index + 1} = {value}",
                    )

    return HintReport(
        board_valid=True,
        board_filled=False,
        message="No hint found",
    )


