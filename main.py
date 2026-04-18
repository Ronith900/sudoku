import copy

from app.generator import generate_puzzle
from app.game import game_is_completed
from app.controller import handle_command
from app.parser import parse_command
from app.render import print_board



def start():
    print("Welcome to Sudoku!\nHere is your puzzle:\n")
    initial_board, solution_board = generate_puzzle()
    board = copy.deepcopy(initial_board)

    while True:
        print_board(board)
        user_response = input("\nEnter command (e.g., A3 4, C5 clear, hint, check, quit): ")
        parsed = parse_command(user_response)

        should_quit = handle_command(parsed, board)
        if should_quit:
            break

        if game_is_completed(board):
            print_board(board)
            print("Congratulations. You have successfully completed the Sudoku puzzle!\n")
            input("Press any key to play once more")


if __name__ == "__main__":
    start()