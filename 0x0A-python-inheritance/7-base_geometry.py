#!/usr/bin/python3
"""class BaseGeometry (based on 6-base_geometry.py)"""


class BaseGeometry:
    def area(self):
        """method to compute"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
