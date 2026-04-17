from dataclasses import dataclass
from collections import defaultdict
from typing import Optional
import re,copy

'''
# Problem statement: MineSweeper App
Write a program that allows a user to play Sudoku on the command line. The program should support puzzle generation, user interaction and validation.

- The game should begin by displaying the Sudoku grid in a readable format, showing 30 pre-filled numbers and empty cells (represented by _ )

- The user can:
	- Enter a number into a specific cell (e.g., B3 7 means place number 7 in row B, column 3).
	- Clear a cell (e.g., C5 clear).
	- Request a hint (e.g., hint) — the program should reveal one correct number.
	- Check the current grid for validity (no duplicates in rows, columns, or subgrids).
	- Quit the game at any time.

- Each move should be validated:
	- The user cannot modify pre-filled cells.
	- The number must be between 1–9.

- The game ends when the grid is completely and correctly filled.
'''

ROW_MAPPING = {'A':0,'B':1,'C':2,"D":3,'E':4,'F':5,'G':6,'H':7,'I':8}
INDEX_TO_ROW = {v:k for k,v in ROW_MAPPING.items()}
PUZZLE = [   ["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]
        ]

@dataclass
class UserInput:
    cell:str
    value:str

@dataclass
class SudokuCheckReport:
    valid: bool
    verdict: str

@dataclass
class HintReport:
    board_valid: bool
    board_filled: bool
    message: str



def get_pre_filled_cells():
    pre_filled_cells = set()
    for r in range(len(PUZZLE)):
        for c in range(len(PUZZLE[r])):
            if PUZZLE[r][c] != ".":
                pre_filled_cells.add(f'{INDEX_TO_ROW[r]}{c+1}')
    return pre_filled_cells

def get_user_object_from_user_response(user_response: str) -> UserInput:
    cell,value = user_response.split(" ")
    return UserInput(cell,value)

def is_user_input_cell_valid(user_input: UserInput) -> bool:
    pre_filled_cells = get_pre_filled_cells()
    return user_input.cell not in pre_filled_cells


def is_user_input_value_valid(user_input: UserInput) -> bool:
    # convert the input string to int obj
    try:
        input_int = int(user_input.value)
        return 1 <= input_int < 10
    except ValueError:
        return False
    

def is_sudoku_grid_valid(board) -> SudokuCheckReport:
    rows = defaultdict(set)
    cols = defaultdict(set)
    grid = defaultdict(set)

    for row_index in range(len(board)):
        for col_index in range(len(board[row_index])):
            cur_value = board[row_index][col_index]

            if cur_value == ".":
                continue
            


            if cur_value in rows[row_index]:
                return SudokuCheckReport(False,f'Number {cur_value} already exists in row {INDEX_TO_ROW[row_index]}')
            elif cur_value in grid[(row_index//3,col_index//3)]:
                return SudokuCheckReport(False,f'Number {cur_value} already exists in 3*3 grid')
            elif cur_value in cols[col_index]:
                return SudokuCheckReport(False,f'Number {cur_value} already exists in column {col_index+1}')  
            
            else:
                rows[row_index].add(cur_value)
                cols[col_index].add(cur_value)
                grid[(row_index//3,col_index//3)].add(cur_value)
    
    return SudokuCheckReport(True,"No rule violations detected.")


def insert_user_input(user_input:UserInput,board):
    new_row = ROW_MAPPING[user_input.cell[0]]
    new_col = int(user_input.cell[1]) - 1
    board[new_row][new_col] = user_input.value
    return board

def remove_user_input(user_input:UserInput,board):
    del_row = ROW_MAPPING[user_input.cell[0]]
    del_col = int(user_input.cell[1]) - 1
    board[del_row][del_col] = "."
    return board

def is_sudoku_board_filled(board):
    required = len(board) * len(board[0])
    needed = 0
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] != ".":
                needed += 1
    return required == needed

def game_is_completed(board):
    board_valid = is_sudoku_grid_valid(board)
    values_filled = is_sudoku_board_filled(board)
    return board_valid.valid and values_filled

def get_candidates(board,row,col):
    if board[row][col] != ".":
        return set()
    digits = set("123456789")
    existing_rows = {board[row][c] for c in range(9) if board[row][c] != "."}
    existing_cols = {board[r][col] for r in range(9) if board[r][col] != "."}
    grid_numbers = {
                        board[r][c]
                        for r in range((row // 3) * 3, (row // 3) * 3 + 3)
                        for c in range((col // 3) * 3, (col // 3) * 3 + 3)
                        if board[r][c] != "."
                    }
    return digits - (existing_rows | existing_cols | grid_numbers)
    

# hint function will only work if the board is valid and the output will be an HintReport object
def hint(board) -> HintReport:
    if not is_sudoku_grid_valid(board).valid:
        return HintReport(board_valid=False,board_filled=False,message="Board is Invalid")
    if is_sudoku_board_filled(board):
        return HintReport(board_valid=True,board_filled=True,message="Board is already complete")
        
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == ".":
                candidates = get_candidates(board,r,c)
                if len(candidates) == 1:
                    value = next(iter(candidates))
                    return HintReport(board_valid=True,board_filled=False,message=f"Hint cell: {INDEX_TO_ROW[r]}{c+1} = {value}")
                        
    
    return HintReport(board_valid=True,board_filled=False,message="No hint found")
    

def print_the_puzzle(board):
    print("Your current grid\n")
    row_labels = "ABCDEFGHI"
    # Column headers
    print("   1 2 3   4 5 6   7 8 9")

    for i, row in enumerate(board):

        # horizontal separator every 3 rows
        if i % 3 == 0 and i != 0:
            print("   " + "-" * 21)

        # Row label
        print(f"{row_labels[i]} ", end=" ")

        for j, val in enumerate(row):

            # vertical separator every 3 cols
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            display = "_" if val == "." else val
            print(display, end=" ")

        print()


if __name__ == "__main__":
    print("Welcome to sudoku!\nHere is your puzzle:\n")
    board = copy.deepcopy(PUZZLE)
    while True:
        # print the current status of the game in the terminal and ask for user response
        print_the_puzzle(board)
        user_response = input("\nEnter command (e.g., A3 4, C5 clear, hint, check,quit):")
        clean_user_response = " ".join(user_response.strip().upper().split())
        
        if clean_user_response == 'CHECK':
            report = is_sudoku_grid_valid(board)
            print(report.verdict)
        elif clean_user_response == 'HINT':
            hint_report = hint(board)
            print(hint_report.message)
        elif re.search(r'CLEAR$',clean_user_response):
            user_input = get_user_object_from_user_response(clean_user_response)
            if is_user_input_cell_valid(user_input):
                remove_user_input(user_input,board)
        elif re.match(r"^[A-I][1-9]\s[1-9]$", clean_user_response):
            user_input = get_user_object_from_user_response(clean_user_response)
            cell_valid = is_user_input_cell_valid(user_input)
            num_valid = is_user_input_value_valid(user_input)
            if not cell_valid:
                print(f'Invalid move. {user_input.cell} is pre-filled.')
            elif not num_valid:
                print(f'Invalid move. {user_input.cell} is outoff bound')
            else:
                insert_user_input(user_input,board)
                print("Move Accepted")
        elif clean_user_response == 'QUIT':
            break
        result = game_is_completed(board)
        if result:
            print_the_puzzle(board)
            print("Congratulations. You have successfully completed the Sudoku puzzle!\n")
            input("Press any key to play once more")
            board = copy.deepcopy(PUZZLE)



    
    
