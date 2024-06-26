#!/usr/bin/python3
"""a class Square."""


class Square:
    """a square."""

    def __init__(self, size=0):
        """new square.
        Args:
            size (int): size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size should be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """current area of the square."""
        return (self.__size * self.__size)
