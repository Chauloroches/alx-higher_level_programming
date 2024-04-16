#!/usr/bin/python3
"""Define read_file function"""


def read_file(filename=""):
    """Read filenane with utf-8"""
        with open(filename, encoding='utf-8') as f
        print(f.read(), end="")
