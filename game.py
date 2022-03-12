#!/usr/bin/python
# -*- coding: utf-8 -*-

import copy
import numpy as np

PLAYER_1 = 1
PLAYER_2 = 2
BOARD = np.zeros((3, 3))

def check_horizontally(board, piece):
    for i in range(3):
        if board[i, 0] == piece and board[i, 1] == piece and board[i,
                2] == piece:
            return True
    return False


def check_vertically(board, piece):
    for i in range(3):
        if board[0, i] == piece and board[1, i] == piece and board[2,
                i] == piece:
            return True
    return False


def check_pos_diagnonal(board, piece):
    if board[0, 0] == piece and board[1, 1] == piece and board[2, 2] \
        == piece:
        return True
    return False


def check_neg_diagnonal(board, piece):
    if board[2, 0] == piece and board[1, 1] == piece and board[0, 2] \
        == piece:
        return True
    return False


def winning_strat(board, piece):
    if check_horizontally(board, piece) == True:
        return True
    elif check_vertically(board, piece) == True:
        return True
    elif check_pos_diagnonal(board, piece) == True:
        return True
    elif check_neg_diagnonal(board, piece) == True:
        return True
    else:
        return False


def is_tie(board, piece):
    if winning_strat(board, piece) == False:
        return True


def score(board):
    if winning_strat(board, PLAYER_1) == True:
        return 10
    elif winning_strat(board, PLAYER_2) == True:
        return -10
    else:
        return 0


def terminal_node(board):
    return winning_strat(board, PLAYER_1) == True \
        or winning_strat(board, PLAYER_2) == True \
        or len(check_empty_spots(board)) == 0


def best_move(board):
    best_score = float('inf')
    move = None
    copy_board = copy.deepcopy(board)
    empty_spot = check_empty_spots(copy_board)
    for (x, y) in empty_spot:
        copy_board = place_piece(copy_board, PLAYER_2, x, y)
        score = minimax(copy_board, 5, True)
        if score < best_score:
            best_score = score
            move = (x, y)
    return move


def minimax(board, depth, max_player):
    empty_cells = check_empty_spots(board)
    terminal = terminal_node(board)

    if depth == 0 or terminal:
        return score(board)
    if max_player:
        val = -float('inf')
        for (x, y) in empty_cells:
            copy_board = copy.deepcopy(board)
            copy_board = place_piece(copy_board, PLAYER_1, x, y)
            new_val = minimax(copy_board, depth - 1, False)
            val = max(new_val, val)
        return val
    else:
        val = float('inf')
        for (x, y) in empty_cells:
            copy_board = copy.deepcopy(board)
            copy_board = place_piece(copy_board, PLAYER_2, x, y)
            new_val = minimax(copy_board, depth - 1, True)
            val = min(new_val, val)
        return val


def print_board(board):
    board_list = []

    arr = board.flatten()
    for x in range(0, 9):
        if arr[x] == 0:
            board_list.append(' ')
        elif arr[x] == 1:
            board_list.append('X')
        elif arr[x] == 2:
            board_list.append('O')
        else:
            raise Exception('Error displaying Board')
    print(""" 
        {} | {} | {}
        {} | {} | {}
        {} | {} | {}
        """.format(*board_list))


def is_valid_move(board, x, y):
    if board[x, y] == 0:
        return True
    return False


def place_piece(
    board,
    piece,
    x,
    y,
    ):
    if is_valid_move(board, x, y) == False:
        print ('Ivalid move, try again')
        return
    board[x, y] = piece
    return board


def check_empty_spots(board):
    empty_list = []
    for x in range(3):
        for y in range(3):
            if board[x, y] == 0:
                empty_list.append((x, y))
    return empty_list


def Player_v_Player():
    turn = PLAYER_1
    global BOARD
    board = BOARD

    while True:
        print_board(board)
        if turn == PLAYER_1:
            pos = input('Player 1, your move (0,0): ')
            (x, y) = [int(x) for x in str(pos).split(',')]
            try:
                board = place_piece(board, PLAYER_1, x, y)
                if winning_strat(board, PLAYER_1) == True:
                    print_board(board)
                    print ('Player 1 wins!')
                    return
                elif is_tie(board, PLAYER_1) == True:
                    print_board(board)
                    print ('TIE')
                    return
                turn = PLAYER_2
            except ValueError:
                print('Empty Value')
        elif turn == PLAYER_2:
            pos = input('Player 2, your move (0,0): ')
            (x, y) = [int(x) for x in str(pos).split(',')]
            try:
                board = place_piece(board, PLAYER_2, x, y)
                if winning_strat(board, PLAYER_2) == True:
                    print_board(board)
                    print ('Player 2 wins!')
                    return
                elif is_tie(board, PLAYER_1) == True:
                    print_board(board)
                    print ('TIE')
                    return
                turn = PLAYER_1
            except ValueError:
                print ('Empty Value')


def Player_v_AI():
    turn = PLAYER_1
    global BOARD
    board = BOARD

    while True:
        print_board(board)
        if turn == PLAYER_1:
            pos = input('Player 1, your move (0,0): ')
            (x, y) = [int(x) for x in str(pos).split(',')]
            try:
                board = place_piece(board, PLAYER_1, x, y)
                if winning_strat(board, PLAYER_1) == True:
                    print_board(board)
                    print ('Player 1 wins!')
                    return
                turn = PLAYER_2
            except ValueError:
                print ('Empty Value')
        elif turn == PLAYER_2:
            print ("AI's turn")
            (x, y) = best_move(board)
            board = place_piece(board, PLAYER_2, x, y)
            try:
                if winning_strat(board, PLAYER_2) == True:
                    print_board(board)
                    print ('AI wins!')
                    return
                turn = PLAYER_1
            except ValueError:
                print ('Empty Value')
