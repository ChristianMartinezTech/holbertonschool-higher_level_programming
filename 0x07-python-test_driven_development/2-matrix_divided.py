#!/usr/bin/python3
"""Python Executable location"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix"""

    ErrInt = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) != list:
        raise TypeError(ErrInt)

    for x in matrix:
        if type(x) != list:
            raise TypeError(ErrInt)

    for x in matrix:
        for y in range(len(x)):
            if not isinstance(y, (int, float)):
                raise TypeError(ErrInt)

    if isinstance(div, (int, float)):
        if div == 0:
            raise ZeroDivisionError("division by zero")
    else:
        raise TypeError("div must be a number")

    if type(div) == bool:
        raise TypeError("div must be a number")

    rows_length = []
    new_matrix = []

    for rows in matrix:
        rows_length.append(len(rows))

    rows_length = set(rows_length)

    if len(rows_length) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    for i in matrix:
        for j in i:
            new_matrix.append(round(j/div, 2))

    return new_matrix
