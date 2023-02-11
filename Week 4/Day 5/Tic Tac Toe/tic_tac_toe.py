

choices = [0, 1, 2, 3, 4, 5, 6, 7, 8]
for x in choices:
    everyChoice = x

def display_board(choices):
    board_gui = f"""
    #############
    # {choices[0]} # {choices[1]} # {choices[2]} #
    #############
    # {choices[3]} # {choices[4]} # {choices[5]} #
    #############
    # {choices[6]} # {choices[7]} # {choices[8]} #
    #############
    """
    print(board_gui)

def switch_players(player: str):
    if player == 'X':
        return 'O'
    else:
        return 'X'

def player_input(player):

    player_choice = None

    while player_choice not in choices:
        player_choice = int(input(f"Player {player} Your choice: "))

    print("Player chose:", player_choice)

    choices[player_choice] = current_player

    display_board(choices)


for i in range(5):
    current_player = 'X'
    player_input(current_player) # X turn

    if choices[0]== "X" and choices[1]== "X" and choices[2]== "X":
        print("X wins!!!")
        break
    elif choices[3]== "X" and choices[4]== "X" and choices[5]== "X":
        print("X wins!!!")
        break
    elif choices[6]== "X" and choices[7]== "X" and choices[8]== "X":
        print("X wins!!!")
        break
    elif choices[0]== "X" and choices[4]== "X" and choices[8]== "X":
        print("X wins!!!")
        break
    elif choices[2]== "X" and choices[4]== "X" and choices[6]== "X":
        print("X wins!!!")
        break
    elif choices[0]== "X" and choices[3]== "X" and choices[6]== "X":
        print("X wins!!!")
        break
    elif choices[1]== "X" and choices[4]== "X" and choices[7]== "X":
        print("X wins!!!")
        break
    elif choices[2]== "X" and choices[5]== "X" and choices[8]== "X":
        print("X wins!!!")
        break
    
    if all(c in ['X', 'O'] for c in choices):
        print("Tie")
        break

    current_player = switch_players(current_player)
    player_input(current_player) # O turn

    if choices[0]== "O" and choices[1]== "O" and choices[2]== "O":
        print("O wins!!!")
        break
    elif choices[3]== "O" and choices[4]== "O" and choices[5]== "O":
        print("O wins!!!")
        break
    elif choices[6]== "O" and choices[7]== "O" and choices[8]== "O":
        print("O wins!!!")
        break
    elif choices[0]== "O" and choices[4]== "O" and choices[8]== "O":
        print("O wins!!!")
        break
    elif choices[2]== "O" and choices[4]== "O" and choices[6]== "O":
        print("O wins!!!")
        break
    elif choices[0]== "O" and choices[3]== "O" and choices[6]== "O":
        print("O wins!!!")
        break
    elif choices[1]== "O" and choices[4]== "O" and choices[7]== "O":
        print("O wins!!!")
        break
    elif choices[2]== "O" and choices[5]== "O" and choices[8]== "O":
        print("O wins!!!")
        break
        
    if all(c in ['X', 'O'] for c in choices):
        print("Tie")
        break
    