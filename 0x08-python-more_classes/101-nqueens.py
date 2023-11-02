#!/usr/bin/python3
""" puzzle queen challenge
"""
from sys import argv, exit


def place(N, row, col, result):
    """ place queens recursively """
    while col < N:
        if isvalid(row, col, result):
            result.append([row, col])
            if row == N-1:
                print(result)
                result.pop()
            else:
                place(N, row+1, 0, result)
        col += 1
    if len(result) > 0:
        result.pop()
    return


def isvalid(row, col, result):
    """ check if the position is valid """
    diag1 = [l[0]+l[1] for l in result]
    diag2 = [l[1]-l[0] for l in result]
    cols = [l[1] for l in result]
    rows = [l[0] for l in result]
    if row in rows or col in cols or row+col in diag1 or col-row in diag2:
        return False
    return True
