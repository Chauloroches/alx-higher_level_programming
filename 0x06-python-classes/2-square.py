#!/usr/bin/python3
"""class square"""

class Square:
    """square"""
    def __init__(self, size =0):
        """new square

        Args:
            size (int): Size of new square
        """
        if not isintance(size, int):
            raise TypeError("Size must be interger")
        elif size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
