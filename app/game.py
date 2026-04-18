from app.constants import ROW_MAPPING, INDEX_TO_ROW
from app.models import UserInput,Hint
from app.validation import is_grid_valid




def insert_user_input(user_input: UserInput, board: list[list[str]]):
    row = ROW_MAPPING[user_input.cell[0]]
    col = int(user_input.cell[1]) - 1

    if board[row][col] == ".":
        board[row][col] = user_input.value

    return board


def remove_user_input(user_input: UserInput,  board: list[list[str]]):
    row = ROW_MAPPING[user_input.cell[0]]
    col = int(user_input.cell[1]) - 1
    board[row][col] = "."
    return board


def hint(current_board:list[list[str]], solution_board:list[list[str]]) -> Hint:
    board_check = is_grid_valid(current_board)
    if not board_check.valid:
        return Hint(
            board_valid=False,
            board_filled=False,
            message="Board is invalid",
        )

    for row_index in range(len(current_board)):
        for col_index in range(len(current_board[row_index])):
            if current_board[row_index][col_index] == ".":
                value = solution_board[row_index][col_index]
                return Hint(
                    board_valid=True,
                    board_filled=False,
                    message=f"Hint: Cell {INDEX_TO_ROW[row_index]}{col_index + 1} = {value}",
                )

    return Hint(
        board_valid=True,
        board_filled=False,
        message="No hint available",
    )


