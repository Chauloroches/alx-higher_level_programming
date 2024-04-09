#!/usr/bin/python3
"""Define function"""
def validate_matrix(matrix):
    if not isinstance(matrix, list):
        raise TypeError("m_a must be a list or m_b must be a list")
    if not matrix:
        raise ValueError("m_a can't be empty or m_b can't be empty")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")
    if not all(row for row in matrix):
        raise ValueError("m_a can't be empty or m_b can't be empty")
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")

def matrix_mul(m_a, m_b):
    validate_matrix(m_a)
    validate_matrix(m_b)

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result

m_a = [[1, 2, 3], [4, 5, 6]]
m_b = [[7, 8], [9, 10], [11, 12]]
result = matrix_mul(m_a, m_b)
print(result)
