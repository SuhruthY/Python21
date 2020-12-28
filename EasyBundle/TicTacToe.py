# ------- Global Variables --------
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_still_going = True # check if game is going
winner = None # Who won? Or tie?
current_player = "X" # Who's turn is it?

## ----- Functions -----
def ask_input(txt):
    ask = input(f"{txt}(Y/N):")
    while ask not in ["Y","y","N","n"]:
        print("Wrong input!")
        ask = input(f"{txt}(Y/N):")
    return ask

# function to display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# func to refresh board
def refresh_board():
    global board

    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]

# function to handle turns amoung players
def handle_turn(player):
    print(f"{player}'s turn.")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("\nWrong input!")
            position = input("Choose a position from 1-9: ")
        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("\nYou can't go there. Go again.")
    board[position] = player

    display_board()

# func to check if game is over
def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    # Set up global variables
    global winner
    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        # there was a win
        winner = row_winner
    elif column_winner:
        # there was a win
        winner = column_winner
    elif diagonal_winner:
        # there was a win
        winner = diagonal_winner
    else:
        # ther was no win
        winner = None
    return

def check_rows():
    # Set up global variables
    global game_still_going
    # check if any of the rows have all the same values (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # Return the winner (X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    # Set up global variables
    global game_still_going
    # check if any of the columns have all the same values (and is not empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # If any column does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # Return the winner (X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    # Set up global variables
    global game_still_going
    # check if any of the diagonals have all the same values (and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    # If any diagonal does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # Return the winner (X or O)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

# func to flip players
def flip_player():
    # global variables we need
    global current_player
    # if the current player was X, then change it to O
    if current_player == "X":
        current_player = "O"
    # if the current player was O, then change it to X
    elif current_player == "O":
        current_player = "X"
    return

# func to main game
def play_game():
    display_board()
    # While the game is still going
    while game_still_going:
        # Handle a single turn of an arbitrary player
        handle_turn(current_player)
        # Check if the game has ended
        check_if_game_over()
        # Flip to the other player
        flip_player()
    # The game has ended
    if winner == "X" or winner == "O":
        print(f"{winner} won.")
    elif winner == None:
        print("Tie.")



## --- MAIN CODE ---
print( "\n","\t\tWElCOME TO\n---- TINKU'S TIC TAC TOE ----\n")

play_game()

run = True
while run:
    game_var = ask_input("Do you wanna play  again?")
    if game_var in ["N", "n"]:
        run = False
    else:
        refresh_board()
        game_still_going = True
        play_game()

print("\n---Game Over---")
