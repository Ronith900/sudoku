import copy

from app.generator import generate_puzzle
from app.controller import handle_command
from app.parser import parse_command
from app.render import print_board
from app.validation import is_game_completed



def start():
    print("Welcome to Sudoku!\nHere is your puzzle:\n")
    sudoku_board, solution_board,pre_filled_cells = generate_puzzle()
    

    while True:
        print_board(sudoku_board)
        user_response = input("\nEnter command (e.g., A3 4, C5 clear, hint, check, quit): ")
        parsed = parse_command(user_response)

        should_quit = handle_command(parsed, sudoku_board,solution_board, pre_filled_cells)
        if should_quit:
            break
        
        if is_game_completed(sudoku_board,solution_board):
            print_board(sudoku_board)
            print("Congratulations. You have successfully completed the Sudoku puzzle!\n")
            input("Press any key to play once more")


if __name__ == "__main__":
    start()