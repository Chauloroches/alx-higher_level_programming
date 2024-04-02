#!/usr/bin/python3
"""Python class MagicClass that does exactly the same as the following Python bytecode"""
import math



class MagicClass:
    """circle"""


    def __int__(self, radius=0):
        """a magicClass

        Arg:
            radius (float or int); radius of the new MagicClass
        """

        self.__radius = 0
        if type(radius) not int and type (radius) not float:
            raise TypeError("radius should be a number")
        self.__radius = radius


        def area(self):
            """the area of the MagicClass"""
            return (self.__radius ** 2 * math.pi)


        def circumference (self):
            """The circumference of the MagicClass"""
            return (2 * math.pi * self.__radius)
