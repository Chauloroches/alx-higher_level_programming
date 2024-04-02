#!/usr/bin/python3
""" class square"""


class Square:
    """square"""
    def __init__(self, size=0):
        """another square"""
        Args:
            size (int): size of new square
        """
        self.size = size


    @property
    def size (self):
        """set the size of square"""
        return (self.__size)


    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = size


    def area(self):
        "current square"
        return (self.__size * self.__size)


