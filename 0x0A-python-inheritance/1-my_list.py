#!/usr/bin/python3
"""Define class MyList that inherits from list"""


class MyList(list):
    def print_sorted(self):
        """printing list method"""
        
        print(sorted(self))

