#!/usr/bin/python3
"""Define save_to_json_file function"""


import json


def save_to_json_file(my_obj, filename):
    """Object to text file"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
