import copy
import random

from app.constants import INDEX_TO_ROW


BOARD_SIZE = 9
SUBGRID_SIZE = 3
EMPTY_CELL = "."

def create_empty_board() -> list[list[str]]:
    return [[EMPTY_CELL for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


def is_valid_placement(board: list[list[str]], row: int, col: int, value: str) -> bool:
    if value in board[row]:
        return False

    for current_row in range(BOARD_SIZE):
        if board[current_row][col] == value:
            return False

    start_row = (row // SUBGRID_SIZE) * SUBGRID_SIZE
    start_col = (col // SUBGRID_SIZE) * SUBGRID_SIZE

    for current_row in range(start_row, start_row + SUBGRID_SIZE):
        for current_col in range(start_col, start_col + SUBGRID_SIZE):
            if board[current_row][current_col] == value:
                return False

    return True


def find_empty_cell(board: list[list[str]]) -> tuple[int, int] | None:
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == EMPTY_CELL:
                return row, col
    return None


def fill_board(board: list[list[str]]) -> bool:
    empty_cell = find_empty_cell(board)

    if empty_cell is None:
        return True

    row, col = empty_cell
    numbers = [str(number) for number in range(1, BOARD_SIZE + 1)]
    random.shuffle(numbers)

    for value in numbers:
        if is_valid_placement(board, row, col, value):
            board[row][col] = value

            if fill_board(board):
                return True

            board[row][col] = EMPTY_CELL

    return False


def remove_cells(board: list[list[str]], cells_to_remove: int) -> list[list[str]]:
    puzzle = copy.deepcopy(board)
    positions = [(row, col) for row in range(BOARD_SIZE) for col in range(BOARD_SIZE)]
    random.shuffle(positions)

    removed = 0

    for row, col in positions:
        if removed == cells_to_remove:
            break

        if puzzle[row][col] != EMPTY_CELL:
            puzzle[row][col] = EMPTY_CELL
            removed += 1

    return puzzle

def get_pre_filled_cells(board:list[list[str]]):
    pre_filled_cells = set()
    for row_index in range(len(board)):
        for col_index in range(len(board[row_index])):
            if board[row_index][col_index] != ".":
                pre_filled_cells.add(f"{INDEX_TO_ROW[row_index]}{col_index + 1}")

    return pre_filled_cells

# need to generate a puzzle which has 30 pre-filled cells for the game to begin
def generate_puzzle(cells_to_remove: int = 51) -> tuple[list[list[str]], list[list[str]]]:
    solution_board = create_empty_board()
    fill_board(solution_board)

    puzzle_board = remove_cells(solution_board, cells_to_remove)
    pre_filled_cells = get_pre_filled_cells(puzzle_board)

    return puzzle_board, solution_board,pre_filled_cells