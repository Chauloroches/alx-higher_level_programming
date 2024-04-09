#!/usr/bin/python3
"""Define afunction"""


def text_indentation(text):
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    chars = {'.', '?', ':'}
    result = ""

    for char in text:

        result += char

        if char in  chars:
            result += "\n\n"

    print(result.strip())

try:
    text_indentation("Hello. I Am Roches. I'm fine, thanks.")
except TypeError as e:
    print(e)
