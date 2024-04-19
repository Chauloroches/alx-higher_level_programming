#!/usr?bin/python3
"""Modele for Base class"""


class Base:
    """Base class for managing id attribute in all classes."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
