#!/usr/bin/python3
"""Define a function"""


def matrix_divided(matrix, div):
    # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) for row in matrix) or \
       not all(isinstance(i, (int, float)) for row in matrix for i in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    
    if div == 0:
        raise ZeroDivisionError("division by zero")

    
    new_matrix = []
    for row in matrix:
        another_row = []
        for i in row:
            another_row.append(round(i / div, 2))
        new_matrix.append(another_row)

    return new_matrix
