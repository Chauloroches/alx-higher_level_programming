#!/usr/bin/python3
"""Define a function"""


def say_my_name(first_name, last_name=""):

    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string"

    print("My name is {} {}".format(first_name, last_name))
