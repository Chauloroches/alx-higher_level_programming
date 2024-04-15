#!/usr/bin/python3
"""Define class MyList that inherits from list"""

lass MyList(list):
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)

