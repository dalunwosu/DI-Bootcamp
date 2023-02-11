choices = [0, 1, 2, 3, 4, 5, 6, 7, 8]

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

while "i" not in "":
    current_player = 'X'
    player_input(current_player)
    
    current_player = switch_players(current_player)

    player_input(current_player)

    




# ***************
# *  0 | 1 | 2  *
# * ---|---|--- *
# *  4 | 5 | 6  *
# * ---|---|--- *
# *  7 | 8 | 9  *
# ***************

# choices = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# for x in choices:
#     everyChoice = x

# def display_board(choices):
#     board_gui = f"""
#     #############
#     # {choices[0]} # {choices[1]} # {choices[2]} #
#     #############
#     # {choices[3]} # {choices[4]} # {choices[5]} #
#     #############
#     # {choices[6]} # {choices[7]} # {choices[8]} #
#     #############
#     """
#     print(board_gui)

# def switch_players(player: str):
#     if player == 'X':
#         return 'O'
#     else:
#         return 'X'

# def player_input(player):

#     player_choice = None

#     while player_choice not in choices:
#         player_choice = int(input(f"Player {player} Your choice: "))

#     print("Player chose:", player_choice)

#     choices[player_choice] = current_player

#     display_board(choices)


# for i in range(5):
#     current_player = 'X'
#     player_input(current_player) # X turn

#     if choices[0]== "X" and choices[1]== "X" and choices[2]== "X":
#         print("X wins!!!")
#         break
#     elif choices[3]== "X" and choices[4]== "X" and choices[5]== "X":
#         print("X wins!!!")
#         break
#     elif choices[6]== "X" and choices[7]== "X" and choices[8]== "X":
#         print("X wins!!!")
#         break
#     elif choices[0]== "X" and choices[4]== "X" and choices[8]== "X":
#         print("X wins!!!")
#         break
#     elif choices[2]== "X" and choices[4]== "X" and choices[6]== "X":
#         print("X wins!!!")
#         break
#     elif choices[0]== "X" and choices[3]== "X" and choices[6]== "X":
#         print("X wins!!!")
#         break
#     elif choices[1]== "X" and choices[4]== "X" and choices[7]== "X":
#         print("X wins!!!")
#         break
#     elif choices[2]== "X" and choices[5]== "X" and choices[8]== "X":
#         print("X wins!!!")
#         break
    
#     if choices[everyChoice] == "O" or choices[everyChoice] == "X":
#         print("tie")
#         break

#     current_player = switch_players(current_player)
#     player_input(current_player) # O turn

#     if choices[0]== "X" and choices[1]== "X" and choices[2]== "X":
#         print("O wins!!!")
#         break
#     elif choices[3]== "X" and choices[4]== "X" and choices[5]== "X":
#         print("O wins!!!")
#         break
#     elif choices[6]== "X" and choices[7]== "X" and choices[8]== "X":
#         print("O wins!!!")
#         break
#     elif choices[0]== "X" and choices[4]== "X" and choices[8]== "X":
#         print("O wins!!!")
#         break
#     elif choices[2]== "X" and choices[4]== "X" and choices[6]== "X":
#         print("O wins!!!")
#         break
#     elif choices[0]== "X" and choices[3]== "X" and choices[6]== "X":
#         print("O wins!!!")
#         break
#     elif choices[1]== "X" and choices[4]== "X" and choices[7]== "X":
#         print("O wins!!!")
#         break
#     elif choices[2]== "X" and choices[5]== "X" and choices[8]== "X":
#         print("O wins!!!")
#         break
        
#     if choices[everyChoice] == "O" or choices[everyChoice] == "X":
#         print("tie")
#         break
    
# ***************
# *  0 | 1 | 2  *
# * ---|---|--- *
# *  4 | 5 | 6  *
# * ---|---|--- *
# *  7 | 8 | 9  *
# ***************
#    