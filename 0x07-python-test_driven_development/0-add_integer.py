#!/usr/bin/python3
""" Define function def add_integer"""

def add_integer(a, b=98):
    # Check if a and b are integers or floats
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
