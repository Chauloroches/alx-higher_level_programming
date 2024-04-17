#!/usr/bin/python3
"""Define class Rectangle"""


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry (7-base_geometry.py)"""
    def __init__(self, width, height):
        """constructor"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

