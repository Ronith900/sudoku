import copy
import re

from constants import PUZZLE
from render import print_the_puzzle
from parser import parse_command
from models import UserInput
from game import (
    game_is_completed,
    get_user_object_from_user_response,
    hint,
    insert_user_input,
    is_user_input_cell_valid,
    is_user_input_value_valid,
    is_sudoku_grid_valid,
    remove_user_input,
)


def run():
    print("Welcome to sudoku!\nHere is your puzzle:\n")
    board = copy.deepcopy(PUZZLE)

    while True:
        print_the_puzzle(board)
        user_response = input("\nEnter command (e.g., A3 4, C5 clear, hint, check,quit):")
        parsed = parse_command(user_response)

        if parsed.action == "check":
            report = is_sudoku_grid_valid(board)
            print(report.verdict)

        elif parsed.action == "hint":
            hint_report = hint(board)
            print(hint_report.message)

        elif parsed.action == "clear":
            user_input = UserInput(parsed.cell,parsed.value)
            if is_user_input_cell_valid(user_input):
                remove_user_input(user_input, board)

        elif parsed.action == "move":
            user_input = UserInput(parsed.cell,parsed.value)
            cell_valid = is_user_input_cell_valid(user_input)
            num_valid = is_user_input_value_valid(user_input)

            if not cell_valid:
                print(f"Invalid move. {user_input.cell} is pre-filled.")
            elif not num_valid:
                print(f"Invalid move. {user_input.cell} is out of bound")
            else:
                insert_user_input(user_input, board)
                print("Move Accepted")

        elif parsed.action == "quit":
            break

        else:
             print("Invalid command")

        result = game_is_completed(board)
        if result:
            print_the_puzzle(board)
            print("Congratulations. You have successfully completed the Sudoku puzzle!\n")
            input("Press any key to play once more")
            board = copy.deepcopy(PUZZLE)


if __name__ == "__main__":
    run()