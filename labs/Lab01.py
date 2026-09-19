# 1. Name:
#      Calvin Griffiths
# 2. Assignment Name:
#      Lab 01: Tic-Tac-Toe
# 3. Assignment Description:
#      Play the game of Tic-Tac-Toe
# 4. What was the hardest part? Be as specific as possible.
#      My hardest part was figuring out how to get around the problem of my computer screen constantly freezing, (In otherwords my computer is cracked and I sometimes have to constantlty close the screen to get it to unfreeze)
# 5. How long did it take for you to complete the assignment?
#      -- It took me aproxiamately 3 hours to complete the required code for the assignment, and then another hour to go above and beyond to figure out how to add score keeping to the game. It also took me a few minutes to get it so the game would play again if the user wanted to play again.--

import json
x_wins = 0
o_wins = 0
ties = 0
# The characters used in the Tic-Tac-Too board.
# These are constants and therefore should never have to change.
X = 'X'
O = 'O'
BLANK = ' '

# A blank Tic-Tac-Toe board. We should not need to change this board;
# it is only used to reset the board to blank. This should be the format
# of the code in the JSON file.
blank_board = {  
            "board": [
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK ]
        }

def read_board(filename):
    '''Read the previously existing board from the file if it exists.'''
    # Put file reading code here.
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data['board']
    except FileNotFoundError:
        return blank_board['board'].copy()

def save_board(filename, board):
    '''Save the current game to a file.'''
    # Put file writing code here.
    data = {
        "board": board
    }

    with open(filename, 'w') as file:
        json.dump(data, file)

def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''
    # Put display code here.
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def is_x_turn(board):
    '''Determine whose turn it is.'''
    # Put code here determining if it is X's turn.
    x_count = board.count(X)
    o_count = board.count(O)

    if x_count == o_count:
        return True  # X's turn
    else:
        return False  # O's turn



def play_game(board):
    '''Play the game of Tic-Tac-Toe.'''
    # Put game play code here. Return False when the user has indicated they are done.

    while not game_done(board):

        display_board(board)

        if is_x_turn(board):
            player = X
        else:
            player = O

        choice = input(f"{player}'s turn. Enter a number from 1 to 9, or 'q' to save, or 'r' to quit: ")

        if choice.lower() == 'q':
            save_board(filename, board)
            print("Game saved. Goodbye!")
            return False
        if choice.lower() == 'r':
            board = blank_board['board'].copy()
            
            return False

        square = int(choice) - 1

        if square < 0 or square > 8:
            print("Please enter a number from 1 to 9.")
            continue

        if board[square] != BLANK:
            print("That square is already taken.")
            continue

        board[square] = player

        # Save the board after every move.
        save_board(filename, board)

    display_board(board)
    game_done(board, True)

    # Determine who won.
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            return board[row * 3]

    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            return board[col]

    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        return board[4]

    return "tie"

def game_done(board, message=False):
    '''Determine if the game is finished.
       Note that this function is provided as-is.
       You do not need to edit it in any way.
       If message == True, then we display a message to the user.
       Otherwise, no message is displayed. '''

    # Game is finished if someone has completed a row.
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True

    # Game is finished if someone has a diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square == BLANK:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True


    return False

# These user-instructions are provided and do not need to be changed.
print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
print("where the following numbers correspond to the locations on the grid:")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 \n")
print("The current board is:")

# The file read code, game loop code, and file close code goes here.
filename = "tic_tac_toe.json"

while True:

    # Read the saved board if one exists.
    board = read_board(filename)

    result = play_game(board)

    # False means the user quit.
    if result == False:
        break

    if result == X:
        x_wins += 1
    elif result == O:
        o_wins += 1
    else:
        ties += 1

    print()
    print("Game totals:")
    print("X wins:", x_wins)
    print("O wins:", o_wins)
    print("Ties:", ties)

    # The game is finished, so reset the saved board.
    board = blank_board['board'].copy()
    save_board(filename, board)

    again = input("Would you like to play again? (y/n): ")

    if again.lower() != 'y':
        break
    