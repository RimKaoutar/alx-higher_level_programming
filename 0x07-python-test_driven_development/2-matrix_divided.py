#!/usr/bin/python3
"""Module for matrix_divided method"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Args:
        matrix: The matrix whoses elements are to be divided by div.
        div: The dividing number.

    Raises:
        TypeError: if matrix is not a list of lists of int or float.
        TypeError: if each row of matrix is not of same size.
        TypeError: if div is neither an int nor float
        ZeroDivisionError: if div is zero

    Returns:
        a new matrix with elements rounded to 2 decimal places.
    """

    if not isinstance(matrix, list)\
        or len(matrix) == 0 or not matrix[0]\
        or all(len(row) == 0 for row in matrix)\
        or not all(isinstance(ele, (int, float))
                   for row in matrix for ele in row):
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")

    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(ele / div, 2) for ele in row] for row in matrix]

    return new_matrix
