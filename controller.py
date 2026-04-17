
from game import (
    hint,
    insert_user_input,
    is_sudoku_grid_valid,
    is_user_input_cell_valid,
    is_user_input_value_valid,
    remove_user_input,
)
from models import UserInput



def handle_command(parsed, board) -> bool:
    if parsed.action == "check":
        report = is_sudoku_grid_valid(board)
        print(report.verdict)
        return False

    if parsed.action == "hint":
        hint_report = hint(board)
        print(hint_report.message)
        return False

    if parsed.action == "clear":
        user_input = UserInput(parsed.cell, parsed.value)
        if is_user_input_cell_valid(user_input):
            remove_user_input(user_input, board)
        else:
            print(f"Invalid move. {user_input.cell} is pre-filled.")
        return False

    if parsed.action == "move":
        user_input = UserInput(parsed.cell, parsed.value)

        if not is_user_input_cell_valid(user_input):
            print(f"Invalid move. {user_input.cell} is pre-filled.")
            return False

        if not is_user_input_value_valid(user_input):
            print(f"Invalid move. {user_input.cell} is out of bound.")
            return False

        insert_user_input(user_input, board)
        print("Move accepted.")
        return False

    if parsed.action == "quit":
        return True

    print("Invalid command.")
    return False

