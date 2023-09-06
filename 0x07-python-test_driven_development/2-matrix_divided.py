#!/usr/bin/python3
# 2-matrix_divided.py
"""Matrix division function."""


def matrix_divided(matrix, div):
    """ Divide every element in the matrix.

    Args:
        matrix: list of lists of ints or floats.
        div: int of float divisor
    Raises:
        TypeError: if elements are non-numeric
        TypeError: rows of different sizes
        TypeError: div is non-numeric
        ZeroDivisionError: div is zero
    Returns:
        new matrix with elements divided by the divisor
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(num, int) or isinstance(num, float))
                    for num in [n for row in matrix for n in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    return ([list(map(lambda n: round(n / div, 2), row)) for row in matrix])
