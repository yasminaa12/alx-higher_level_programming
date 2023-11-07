#!/usr/bin/python3
"""Defines a Pascal's Triangle function"""


def pascal_triangle(n):
    """Representation of a Pascal's Triangle of size n"""

    if n <= 0:
        return []

    Triangle = [[1]]

    while len(Triangle) != n:
        tri = Triangle[-1]
        tmp = [1]
        for j in range(len(tri) - 1):
            tmp.append(tri[j] + tri[j + 1])
        tmp.append(1)
        Triangle.append(tmp)

    return Triangle
