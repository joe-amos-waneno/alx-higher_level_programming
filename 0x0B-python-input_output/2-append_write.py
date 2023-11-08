#!/usr/bin/python3
"""write a string to  text file"""


def write_file(filename="", text=""):
    """append a text to a file."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
