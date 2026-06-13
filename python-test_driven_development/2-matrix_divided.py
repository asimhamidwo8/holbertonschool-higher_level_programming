#!/usr/bin/python3
"""Module that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix"""

    error = "matrix must be a matrix (list of lists) of integers/floats"

    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(error)

    row_size = len(matrix[0])

    for row in matrix:
        if len(row) != row_size:
            raise TypeError(
                "Each row of the matrix must have the same size"
            )

        for value in row:
            if not isinstance(value, (int, float)):
                raise TypeError(error)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [
        [round(value / div, 2) for value in row]
        for row in matrix
    ]
