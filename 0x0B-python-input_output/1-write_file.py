#!/usr/bin/python3
"""wites  string to  a text file"""


def write_file(filename="", text=""):
    """write to  the file."""
    with open(filename, 'w') as file:
        return file.write(text)
