"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xcount = 0
    ocount = 0
    for i in board:
        for j in i:
            if j == X:
                xcount += 1
            if j == O:
                ocount += 1
    if terminal(board) == True:
        return 3
    if xcount == ocount:
        return X
    if xcount - 1 == ocount:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    all_positions = {(0, 0), (0, 1), (0, 2),
                     (1, 0), (1, 1), (1, 2),
                     (2, 0), (2, 1), (2, 2)}
    for i in range(3):
        for j in range(3):
            if board[i][j] == X or board[i][j] == O:
                all_positions.discard((i, j))
    return all_positions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    
    if board[i][j] is not None:
        raise ValueError("Invalid action: Cell is already occupied")

    # Determine the player whose turn it is
    current_player = player(board)

    # Make a deep copy of the board
    new_board = copy.deepcopy(board)

    # Apply the action to the new board
    new_board[i][j] = current_player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not EMPTY:
            return row[0]
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not EMPTY:
            return board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]
    # No winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    else:
        x = 1
        for i in board:
            for j in i: 
                if j == None:
                    x = 0
        if x == 0:
            return False
        else:
            return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if ((terminal(board) == True) and (winner(board) == X)):
        return 1
    elif ((terminal(board) == True) and (winner(board) == O)):
        return -1
    elif ((terminal(board) == True) and (winner(board) == None)):
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = min_value(result(board, action))
        if aux > v:
            v = aux
            move = action
            if v == 1:
                return v, move

    return v, move


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = max_value(result(board, action))
        if aux < v:
            v = aux
            move = action
            if v == -1:
                return v, move

    return v, move