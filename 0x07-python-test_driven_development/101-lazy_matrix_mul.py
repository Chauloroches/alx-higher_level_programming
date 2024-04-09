#!/usr/bin/python3
import numpy as np
"""DEfine function"""


def lazy_matrix_mul(m_a, m_b):
    try:
        np_m_a = np.array(m_a)
        np_m_b = np.array(m_b)
        result = np.dot(np_m_a, np_m_b)
        return result.tolist()
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")

# Example usage:
m_a = [[1, 2, 3], [4, 5, 6]]
m_b = [[7, 8], [9, 10], [11, 12]]
result = lazy_matrix_mul(m_a, m_b)
print(result)
