from dataclasses import dataclass
from collections import defaultdict
from typing import Optional

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



@dataclass
class UserInput:
    cell:str
    value:Optional[str] = None


def get_initial_grid():
    return [ ["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]
        ]


def get_pre_filled_cells():
    board = get_initial_grid()
    pre_filled_cells = set()
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] != ".":
                pre_filled_cells.add(f'{INDEX_TO_ROW[r]}{c+1}')
    return pre_filled_cells



def is_user_input_cell_valid(user_input: UserInput):
    pre_filled_cells = get_pre_filled_cells()
    return user_input.cell not in pre_filled_cells


def is_user_input_value_valid(user_input: UserInput):
    # convert the input string to int obj
    try:
        input_int = int(user_input.value)
        return 1 <= input_int < 10
    except ValueError:
        return False
    

def is_sudoku_grid_valid(board):
    rows = defaultdict(set)
    cols = defaultdict(set)
    grid = defaultdict(set)

    for row_index in range(len(board)):
        for col_index in range(len(board[row_index])):
            cur_value = board[row_index][col_index]

            if cur_value == ".":
                continue
            
            if cur_value in rows[row_index]:
                return (False,f'Number {cur_value} already exists in row {INDEX_TO_ROW[row_index]}')
            elif cur_value in cols[col_index]:
                return (False,f'Number {cur_value} already exists in column {col_index+1}')
            elif cur_value in grid[(row_index//3,col_index//3)]:
                return (False,f'Number {cur_value} already exists in 3*3 grid')
            else:
                rows[row_index].add(cur_value)
                cols[col_index].add(cur_value)
                grid[(row_index//3,col_index//3)].add(cur_value)
    
    return True


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


# def print_the_puzzle(board):
#     for i, row in enumerate(grid):
#         if i % 3 == 0 and i != 0:
#             print("-" * 21)

#         for j, val in enumerate(row):
#             if j % 3 == 0 and j != 0:
#                 print("|", end=" ")

#             print(val, end=" ")

#         print()



if __name__ == "__main__":
    print("Welcome to sudoku!")

    while True:
        grid = get_initial_grid()
        response = input("Enter command (e.g., A3 4, C5 clear, hint, check):")
        if response == 'q':
            break
        print(f"User response is {response}")
        


    
    
