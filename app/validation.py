from app.models import UserInput,SudokuCheckReport,CellPrefilled
from collections import defaultdict
from app.constants import INDEX_TO_ROW


def is_cell_prefilled(user_input: UserInput,pre_filled_cells: set) -> CellPrefilled:
    if user_input.cell in pre_filled_cells:
        return CellPrefilled(True,f'Invalid move. {user_input.cell} is pre-filled.')
    return CellPrefilled(False,f'Move accepted')


def is_grid_valid(board: list[list[str]]) -> SudokuCheckReport:
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



def is_game_completed(current_board: list[list[str]],solution_board:list[list[str]]) -> bool:
    return current_board == solution_board

