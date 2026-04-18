from app.generator import (
    create_empty_board,
    is_valid_placement,
    find_empty_cell,
    fill_board,
    remove_cells,
    get_pre_filled_cells,
    generate_puzzle,
)
from app.validation import is_grid_valid


def test_create_empty_board_returns_9x9_board():
    board = create_empty_board()

    assert len(board) == 9
    assert all(len(row) == 9 for row in board)
    assert all(cell == "." for row in board for cell in row)


def test_is_valid_placement_returns_true_for_valid_value():
    board = create_empty_board()

    result = is_valid_placement(board, 0, 0, "5")

    assert result is True


def test_is_valid_placement_returns_false_if_value_exists_in_row():
    board = create_empty_board()
    board[0][3] = "5"

    result = is_valid_placement(board, 0, 0, "5")

    assert result is False


def test_is_valid_placement_returns_false_if_value_exists_in_column():
    board = create_empty_board()
    board[4][0] = "5"

    result = is_valid_placement(board, 0, 0, "5")

    assert result is False


def test_is_valid_placement_returns_false_if_value_exists_in_subgrid():
    board = create_empty_board()
    board[1][1] = "5"

    result = is_valid_placement(board, 0, 0, "5")

    assert result is False


def test_find_empty_cell_returns_first_empty_position():
    board = [
        ["5", "3", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ]

    result = find_empty_cell(board)

    assert result == (0, 2)


def test_find_empty_cell_returns_none_when_board_is_full():
    board = [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
    ]

    result = find_empty_cell(board)

    assert result is None


def test_fill_board_returns_true_for_empty_board():
    board = create_empty_board()

    result = fill_board(board)

    assert result is True
    assert all(cell != "." for row in board for cell in row)


def test_fill_board_creates_valid_sudoku_board():
    board = create_empty_board()
    fill_board(board)

    result = is_grid_valid(board)

    assert result.valid is True


def test_remove_cells_removes_requested_number_of_cells():
    board = [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
    ]

    puzzle = remove_cells(board, 10)

    empty_cells = sum(1 for row in puzzle for cell in row if cell == ".")

    assert empty_cells == 10


def test_remove_cells_does_not_modify_original_board():
    board = [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
    ]

    original_copy = [row[:] for row in board]

    _ = remove_cells(board, 10)

    assert board == original_copy


def test_get_pre_filled_cells_returns_expected_cells():
    board = [
        ["5", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", "7", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", "8", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "9"],
    ]

    result = get_pre_filled_cells(board)

    assert result == {"A1", "B2", "C3", "I9"}


def test_generate_puzzle_returns_puzzle_solution_and_prefilled_cells():
    puzzle_board, solution_board, pre_filled_cells = generate_puzzle()

    assert len(puzzle_board) == 9
    assert len(solution_board) == 9
    assert isinstance(pre_filled_cells, set)


def test_generate_puzzle_returns_valid_solution_board():
    _, solution_board, _ = generate_puzzle()

    result = is_grid_valid(solution_board)

    assert result.valid is True


def test_generate_puzzle_returns_puzzle_with_51_empty_cells_by_default():
    puzzle_board, _, _ = generate_puzzle()

    empty_cells = sum(1 for row in puzzle_board for cell in row if cell == ".")

    assert empty_cells == 51


def test_generate_puzzle_returns_30_prefilled_cells_by_default():
    _, _, pre_filled_cells = generate_puzzle()

    assert len(pre_filled_cells) == 30


def test_generate_puzzle_prefilled_cells_match_puzzle_board():
    puzzle_board, _, pre_filled_cells = generate_puzzle()

    expected_cells = get_pre_filled_cells(puzzle_board)

    assert pre_filled_cells == expected_cells