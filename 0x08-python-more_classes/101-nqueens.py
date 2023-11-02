#!/usr/bin/python3
"""the N-queens puzzle"""

import sys


def Board_init(n):
    """Initialize  `n`x`n` sized chessboard with 0's"""

    the_board = []
    [the_board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in the_board]
    return the_board


def Deep_copy_board(board):
    """Return deepcopy of a chessboard"""

    if isinstance(board, list):
        return list(map(Deep_copy_board, board))
    return (board)


def Gets_solution(board):
    """Return list of lists representation of a solved chessboard"""

    solve = []
    for a in range(len(board)):
        for b in range(len(board)):
            if board[a][b] == "Q":
                solve.append([a, b])
                break
    return solve


def nbr_out(board, row, col):
    """nbr out spots on a chessboard

    the Args:
        board (list): current working chessboard
        row (int): row where a queen was last played
        col (int): column where a queen was last played
    """
    # nbr out all forward spots
    for b in range(col + 1, len(board)):
        board[row][b] = "x"
    # nbr out all backwards spots
    for b in range(col - 1, -1, -1):
        board[row][b] = "x"
    # nbr out all spots below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # nbr out all spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # nbr out all spots diagonally down to the right
    b = col + 1
    for r in range(row + 1, len(board)):
        if b >= len(board):
            break
        board[r][b] = "x"
        b += 1
    # nbr out all spots diagonally up to the left
    b = col - 1
    for r in range(row - 1, -1, -1):
        if b < 0:
            break
        board[r][b]
        b -= 1
    # nbr out all spots diagonally up to the right
    b = col + 1
    for r in range(row - 1, -1, -1):
        if b >= len(board):
            break
        board[r][b] = "x"
        b += 1
    # nbr out all spots diagonally down to the left
    b = col - 1
    for r in range(row + 1, len(board)):
        if b < 0:
            break
        board[r][b] = "x"
        b -= 1


def Solve_recursive(board, row, Queens_placed, solutions):
    """Recursively solve N-queens puzzle

    the Args:
        board (list): current working chessboard
        row (int): current working row
        queens (int):  current number of placed queens
        solutions (list): list of lists of solutions
    Returns:
        solutions
    """

    if Queens_placed == len(board):
        solutions.append(Gets_solution(board))
        return (solutions)

    for b in range(len(board)):
        if board[row][b] == " ":
            Board_tmp = Deep_copy_board(board)
            Board_tmp[row][b] = "Q"
            nbr_out(Board_tmp, row, b)
            solutions = Solve_recursive(Board_tmp, row + 1,
                                        Queens_placed + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    the_board = Board_init(int(sys.argv[1]))
    solutions = Solve_recursive(the_board, 0, 0, [])
    for sol in solutions:
        print(sol)
