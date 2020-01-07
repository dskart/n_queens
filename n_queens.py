import copy
import scipy.special

from abc import ABC, abstractmethod


def num_placements_all(n):
    num_board_tiles = n * n
    return scipy.special.binom(num_board_tiles, n)


def num_placements_one_per_row(n):
    return n ** n


def n_queens_valid(board):
    if len(board) == 1:
        return True

    seen = set()
    for column in board:
        if column in seen:
            return False
        seen.add(column)

    descending_diagonal = list(board[i]+i for i in range(len(board)))
    seen = set()
    for addition in descending_diagonal:
        if addition in seen:
            return False
        seen.add(addition)

    ascending_diagonal = list(board[i]-i for i in range(len(board)))
    seen = set()
    for addition in ascending_diagonal:
        if addition in seen:
            return False
        seen.add(addition)

    return True


def n_queens_solutions(n):
    board = []
    for solutions in n_queens_helper(board, 0, n):
        yield solutions.copy()


def n_queens_helper(board, depth, n):

    if depth == n:
        yield board
    else:
        board.append(None)
        for i in range(n):

            board[depth] = i
            if (n_queens_valid(board)):
                for i in n_queens_helper(board, depth+1, n):
                    yield i
        del board[-1]
