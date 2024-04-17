#!/usr/bin/python3
"""class MyInt that inherits from int"""


class MyInt(int):
    """MyInt is a rebel. MyInt has == and != operators inverted"""
    def __eq__(self, other):
        # Invert the behavior of ==
        return super().__ne__(other)

    def __ne__(self, other):
        # Invert the behavior of !=
        return super().__eq__(other)
