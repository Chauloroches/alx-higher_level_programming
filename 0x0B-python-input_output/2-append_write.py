#!/usr/bin/python3
"""Define append_write function"""


def append_write(filename="", text=""):
    """append with utf-8"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
