
from main import remove_user_input,is_user_input_cell_valid,is_user_input_value_valid,UserInput,is_sudoku_grid_valid,insert_user_input
import pytest


# This test function will check if input cell is part of the pre-filled values
@pytest.mark.parametrize("user_input, expected",[(UserInput("A1",6),False),(UserInput("B2",6),True)])
def test_is_user_input_move_valid(user_input,expected):
    result = is_user_input_cell_valid(user_input)
    assert result == expected

# This test function will validate if the user input number is in between 1-9, decimal values will be rejected, 
# if the object is not in it will be rejected
@pytest.mark.parametrize("user_input, expected",[(UserInput("A1","6"),True),(UserInput("A2","100"),False),
                                                 (UserInput("A2","2.5"),False),
                                                 (UserInput("A1","a"),False),
                                                 (UserInput("A3","9"),True)])
def test_is_user_input_value_valid(user_input,expected):
    result = is_user_input_value_valid(user_input)
    assert result == expected


def test_insert_user_input():
    user_input = UserInput("A3","2")
    input = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]
        ]
    output = [["5","3","2",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]
        ]
    result = insert_user_input(user_input,input)
    assert result == output

def test_remove_user_input():
    user_input = UserInput("A3")
    input = [["5","3","7",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]
        ]
    output = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]
        ]
    result = remove_user_input(user_input,input)
    assert result == output

def test_if_sudoku_grid_valid_pass():
    input = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]
            ]
    result = is_sudoku_grid_valid(input)
    assert result == True

def test_if_sudoku_grid_valid_fail():
    input = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    result = is_sudoku_grid_valid(input)
    assert result == (False,"Number 8 already exists in 3*3 grid")

