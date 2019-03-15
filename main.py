import os
import sys
import random


def player_marker_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1, pick X or O:').upper()

    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def display_board():
    global board

    os.system('cls') if sys.platform.startswith('win32') else os.system('clear')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-- --- --')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-- --- --')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])


def player_input():
    position = 0
    global last_chance
    global board

    if last_chance == player2:
        player = player1
        last_chance = player1
    else:
        player = player2
        last_chance = player2

    while position not in range(1, 10) or board[position] != ' ':
        position = int(input(f'{player}, your turn. Enter your position from 1 to 9: '))

    place_marker(player, position)


def place_marker(marker, position):
    global board

    board[position] = marker
    display_board()


def win_check():
    player1_positions = set()
    player2_positions = set()
    win_conditions = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {3, 5, 7}, {1, 5, 9}]

    for position, marker in enumerate(board):
        if marker == player1:
            player1_positions.add(position)
        elif marker == player2:
            player2_positions.add(position)

    for condition in win_conditions:
        if condition <= player1_positions:
            print('Player 1 won! Wohoo!')
            return True
        elif condition <= player2_positions:
            print('Player 2 won! Wohoo!')
            return True

    if full_board_check():
        print("It's a tie!")
        return True

    return False


def full_board_check():
    global board

    for position in board:
        if position == ' ':
            return False
    return True


def replay():
    replay_game = ' '
    while replay_game.lower() not in 'yn':
        replay_game = input('Do you want to play again? Y or N:')

    return replay_game.lower() == 'y'


def choose_first_player():
    global last_chance
    chosen_integer = random.randint(1, 2)

    if chosen_integer == 1:
        print('Player 1 goes first')
        last_chance = player2
    else:
        print('Player 2 goes first')
        last_chance = player1


print('Welcome to Tic Tac Toe!\n')
print('Rules:\n')
print('1. The game is played on a 3x3 grid with grids numbered from 1 to 9 as shown:')
print('7 | 8 | 9')
print('-- --- --')
print('4 | 5 | 6')
print('-- --- --')
print('1 | 2 | 3\n')
print('2. Two players, one X and one O play the game.\n')
print('3. A player is selected at random to begin the game.\n')
print('3. The first player to get 3 of their marks in a row - vertically, horizontally or diagonally wins the game.\n')
print('4. The game is a tie if no one wins.\n')
print("Ready? Let's begin! \n\n")

while True:
    last_chance = ''
    board = [' '] * 10
    board[0] = '#'

    player1, player2 = player_marker_input()
    choose_first_player()
    while not win_check() and not full_board_check():
        player_input()
    if not replay():
        print('Thanks for playing! Have a nice day')
        break
