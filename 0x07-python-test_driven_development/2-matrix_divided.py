#!/usr/bin/python3
"""
Supplies a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Args:
        matrix: the matrix provided.
        div: the divisor.

    Raises:
        TypeError: if matrix is not a list of lists, if rows are not lists of
        integers or floats, if rows are not same size.
        ZeroDivisonError: if div == 0.

    Returns: a new matrix.
    """
    if div == 0:
        raise ZeroDivisionError('division by zero')

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if (not isinstance(matrix, list) or matrix == [] or
            not (isinstance(row, list) for row in matrix) or
            not all((isinstance(x, (int, float)) or isinstance(x, int))
                    for x in [num for row in matrix for num in row])):
        raise TypeError('matrix must be a matrix (list of lists)'
                        ' of integers/floats')
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
