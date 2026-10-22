# 1. Name:
#      Calvin Griffiths
# 2. Assignment Name:
#      Lab 06 : Sudoku Program
# 3. Assignment Description:
#      This program is meant to be used to allow a user to solve Sudoku puzzles.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was getting the program to check if the user input was valid and then to check if the number the user input was valid for the cell they selected. I had to make sure that the program would check the row, column, and 3x3 square for any duplicates of the number the user input. 
# 5. How long did it take for you to complete the assignment?
#      4 hours

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

def get_legal_values(board, row, column):
    '''Return all numbers that can legally go in a cell.'''
    legal_values = []

    for number in range(1, 10):
        is_valid = True

        # Check the selected row.
        for j in range(9):
            if j != column and board[row][j] == number:
                is_valid = False
                break

        # Check the selected column.
        if is_valid:
            for i in range(9):
                if i != row and board[i][column] == number:
                    is_valid = False
                    break

        # Find the top-left corner of the 3x3 square.
        box_row = (row // 3) * 3
        box_column = (column // 3) * 3

        # Check the selected 3x3 square.
        if is_valid:
            for i in range(box_row, box_row + 3):
                for j in range(box_column, box_column + 3):
                    if (i != row or j != column) and board[i][j] == number:
                        is_valid = False
                        break

                if not is_valid:
                    break

        # Add the number if it passes all three checks.
        if is_valid:
            legal_values.append(number)

    return legal_values


def enter_number(board):
    '''Allow the user to enter a number into a cell.'''
    coordinate = input(
        "\nEnter a cell coordinate, 'S' to save, or 'Q' to quit without saving: "
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

    number = input("Enter a number (1-9, 'hint' for legal values, or 0 to clear the cell): ").strip()

    if number.lower() == 'hint':
        legal_values = get_legal_values(board, row, column)

        if legal_values:
            print(f"Legal values for cell {coordinate}: {legal_values}")
        else:
            print(f"No legal values available for cell {coordinate}.")
        return None

    if len(number) != 1 or number not in "0123456789":
        print("Invalid number. Please enter a digit from 0 to 9 or 'hint'.")
        return None

    
    number = int(number)

    if number == 0:
        board[row][column] = 0
        print(f"{coordinate} Cleared! ")
        return None
    
    # Check the row, column, and 3x3 square.
    legal_values = get_legal_values(board, row, column)

    if number != 0 and number not in legal_values:
        print(
            f"Invalid move! {number} already appears in the "
            "selected row, column, or 3x3 square. Please try again."
            )
        return None
    
    board[row][column] = number

    print(f"{coordinate} updated!")
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