#!/usr/bin/python3
"""Define class Student"""


class Student:
    """Represent student"""
    def __init__(self, first_name, last_name, age):
        """student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Dictionary representing student"""
        return self.__dict__
