#!/usr/bin/python3
"""FUNCTION def pascal_triangle"""


def pascal_triangle(n):
    """Pascal triangle size n"""
    if n <= 0:
        return []

    triangle = [[1]]
    for a in range(1, n):
        row = triangle[-1]
        new_row = [1]  
        for b in range(1, a):
            new_row.append(row[b - 1] + row[b])  
        new_row.append(1)  
        triangle.append(new_row)

    return triangle

