#!/usr/bin/python3
""Define class Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """intiate a student obj"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Dictionary rep of a student"""
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
