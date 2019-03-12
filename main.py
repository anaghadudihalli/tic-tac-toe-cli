import os
import sys


def player_marker_input():
    player1 = ''

    while player1 != 'X' and player1 != 'O':
        player1 = input('Player 1, pick X or O:')

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return player1, player2


def display_board():
    os.system('cls') if sys.platform.startswith('win32') else os.system('clear')

    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-- --- --')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-- --- --')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])


def player_input(player):
    while True:
        position = int(input('{player}, your turn. Enter your position from 1 to 9: '))

        if board[position] == ' ':
            place_marker(player, position)
            break


def place_marker(marker, position):
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
            print('player 1 won')
        elif condition <= player2_positions:
            print('player 2 won')


board = [' '] * 10
player1, player2 = player_marker_input()
player_input()

