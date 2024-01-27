"""
Tic tac toe input
Here's the backstory for this challenge: imagine you're writing a tic-tac-toe game, where the board looks like this:

1:  X | O | X
   -----------
2:    |   |  
   -----------
3:  O |   |

    A   B  C
The board is represented as a 2D list:

board = [
    ["X", "O", "X"],
    [" ", " ", " "],
    ["O", " ", " "],
]
Imagine if your user enters "C1" and you need to see if there's an X or O in that cell on the board. To do so, you need to translate from the string "C1" to row 0 and column 2 so that you can check board[row][column].

Your task is to write a function that can translate from strings of length 2 to a tuple (row, column). Name your function get_row_col; it should take a single parameter which is a string of length 2 consisting of an uppercase letter and a digit.

For example, calling get_row_col("A3") should return the tuple (2, 0) because A3 corresponds to the row at index 2 and column at index 0in the board.
"""

# solution 1
def get_row_col1(string):
    
    # get the 2 parameters from the given string
    column = string[0].lower()
    row = int(string[1]) - 1

    # translate letter to indecolumn number (row number)
    if column == "a":
        column = 0
    elif column == "b":
        column = 1
    else:
        column = 2

    return (row, column)

# Short version (pythonprinciples.com solution)
def get_row_col2(string):
    row = int(string[1]) - 1
    letter = string[0].lower()
    translate = {"a":0, "b":1, "c":2}
    column = translate[letter]
    return (row, column)
            
string = "A3"

print(get_row_col1(string))
print(get_row_col2(string))