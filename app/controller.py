
from app.game import insert_user_input,remove_user_input,hint
from app.validation import is_grid_valid,is_cell_prefilled
from app.models import UserInput


def handle_command(parsed, board,solution_board,pre_filled_cells) -> bool:
    if parsed.action == "check":
        report = is_grid_valid(board)
        print(report.verdict)
        return False

    if parsed.action == "hint":
        hint_report = hint(board,solution_board)
        print(hint_report.message)
        return False

    if parsed.action == "clear":
        user_input = UserInput(parsed.cell, parsed.value)
        cell_prefilled = is_cell_prefilled(user_input,pre_filled_cells)
        if not cell_prefilled.is_prefilled:
            remove_user_input(user_input, board)
        else:
            print(cell_prefilled.message)
        
        return False

    if parsed.action == "move":
        user_input = UserInput(parsed.cell, parsed.value)
        cell_prefilled = is_cell_prefilled(user_input,pre_filled_cells)
        
        if not cell_prefilled.is_prefilled:
            insert_user_input(user_input, board)
        else:
            print(cell_prefilled.message)

        return False

    if parsed.action == "quit":
        return True

    print("Invalid command.")
    return False

