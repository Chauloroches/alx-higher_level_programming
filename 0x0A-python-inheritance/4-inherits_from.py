#!/usr/bin/python3
"""Define function returns True if the object is an instance of a class that inherited 
(directly or indirectly) from the specified class ; otherwise False
"""
def inherits_from(obj, a_class):
    return issubclass(obj.__class__, a_class) and obj.__class__ != a_class
