#!/usr/bin/python3
"""
This module provides the function matrix_divided
that divide all elelements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    matrix_divided - Performs the division of all elements of each rowin matrix

    matrix -- list of lists of integer or/and floats
    div -- The number that divide the integer of each row

    This function checks if matrix is a list else throws an error
    checks if each row of matrix are a list eles throws an error
    checks if each row are the same size otherwise an error throwed
    checks if div is a number and is different of zero else throws an error
    """

    list_error = "matrix must be a matrix (list of lists) of integers/floats"
    length_error = "Each row of the matrix must have the same size"
    div_zero_error = "division by zero"

    if not (isinstance(matrix, list)):
        raise TypeError(list_error)
    for row in matrix:
        if not (isinstance(row, list)):
            raise TypeError(list_error)
        length = len(row)
        for i in row:
            if not TypeError(isinstance(i, (int, float))):
                raise TypeError(list_error)
    for row in matrix:
        if len(row) != length:
            raise TypeError(length_error)
    if not (isinstance(div, (int, float))):
        raise TypeError("div must be a number")
    if div == 0:
        raise (div_zero_error)
    new_matrix = []
    for row in matrix:
        new_matrix.append(list(map(lambda x: round(x / div, 2), row)))
    return new_matrix
