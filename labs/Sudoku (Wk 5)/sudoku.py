# 1. Name:
#      Calvin Griffiths
# 2. Assignment Name:
#      Lab 05 : Sudoku Draft
# 3. Assignment Description:
#      This program is meant to be used to allow a user to solve Sudoku puzzles.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was getting the program to check if the user input was valid and then to check if the puzzle was solved correctly. I had to figure out how to check if the numbers in each row, column, and 3x3 box were unique and within the range of 1-9. I also had to figure out how to handle invalid input from the user, such as entering a number that is already in the row, column, or box.
# 5. How long did it take for you to complete the assignment?
#      3 hours

import json

# A blank Sudoku board. We should not need to change this board; it is only used to reset the board to blank. This should be the format of the code in the JSON file.
blank_board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]
resume = input("Would you like to resume a previous game? (yes/no): ").lower()

if resume == 'yes':
    save_filename = input(
        "Enter the saved game filename "
        "(e.g., 131.05.Easy.Save.json, 131.05.Medium.Save.json, 131.05.Hard.Save.json): "
    ).strip()

    if save_filename.endswith(".Save.json"):
        filename = save_filename.replace(".Save.json", ".json")
    else:
        filename = save_filename
        save_filename = filename[:-5] + ".Save.json"

else:
    difficulty = input(
        "Enter the difficulty level you would like to challenge "
        "(easy, medium, hard): "
    ).lower()

    if difficulty not in ['easy', 'medium', 'hard']:
        print("Invalid difficulty level. Please choose from easy, medium, or hard.")
        exit()

    if difficulty == 'easy':
        filename = '131.05.Easy.json'
    elif difficulty == 'medium':
        filename = '131.05.Medium.json'
    else:
        filename = '131.05.Hard.json'

    save_filename = filename[:-5] + ".Save.json"

def read_board(filename, fallback_board=None):
    '''Read a board from a file, or use a fallback board if it doesn't exist.'''
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data['board']
    except FileNotFoundError:
        if fallback_board is not None:
            return [row.copy() for row in fallback_board]
        return [row.copy() for row in blank_board]

def save_board(filename, board):
    '''Save the current game to a file.'''
    data = {
        "board": board
    }
    with open(filename, 'w') as file:
        json.dump(data, file)

def display_board(board):
    '''Display a Sudoku board with coordinate labels.'''
    print()

    #Display column labels (A-I)
    print("   A B C   D E F   G H I")

    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("  " + "-" * 25)

        #Display row labels (1-9)
        print(i + 1, end="| ")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if board[i][j] == 0:
                print(" ", end=" ")
            else:
                print(board[i][j], end=" ")
        print()

def get_cell_coordinates(coordinate):
    '''Convert a cell coordinate into column and row indices.'''
    coordinate = coordinate.upper()

    if len(coordinate) != 2:
        return None

    if coordinate[0].isalpha():
        column_letter = coordinate[0]
        row_number = coordinate[1]
    else:
        row_number = coordinate[0]
        column_letter = coordinate[1]

    if column_letter not in "ABCDEFGHI":
        return None

    if row_number not in "123456789":
        return None

    column = ord(column_letter) - ord("A")
    row = int(row_number) - 1

    return column, row

def enter_number(board):
    '''Allow the user to enter a number into a cell.'''
    coordinate = input(
        "Enter a cell coordinate, 'S' to save, "
        "or 'Q' to quit without saving: "
    ).strip().upper()

    if coordinate == 'S':
        return 'save'

    if coordinate == 'Q':
        return 'quit'

    coordinates = get_cell_coordinates(coordinate)

    if coordinates is None:
        print("Invalid coordinate. Please try again.")
        return None

    column, row = coordinates

    if original_board[row][column] != 0:
        print("You cannot change an original puzzle clue.")
        return None

    number = input("Enter a number (1-9, or 0 to clear the cell): ").strip()

    if len(number) != 1 or number not in "0123456789":
        print("Invalid number. Please enter a digit from 0 to 9.")
        return None

    board[row][column] = int(number)

    print("Cell updated!")
    return None

# Load the original puzzle separately.
original_board = read_board(filename)

# Load the saved game, or start from the original puzzle.
if resume == 'yes':
    board = read_board(save_filename, original_board)
else:
    board = [row.copy() for row in original_board]

while True:
    display_board(board)

    action = enter_number(board)

    if action == 'save' or action == 's':
        save_board(save_filename, board)
        print(f"Game saved to {save_filename}.")
        break

    elif action == 'quit' or action == 'q':
        print("Game closed without saving.")
        break