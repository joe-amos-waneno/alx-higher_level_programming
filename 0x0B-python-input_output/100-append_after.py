#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.
    Args:
        filename (str): name of the file.
        search_string (str): string to search for within the file.
        new_string (str): string to insert.
    """
    msg = ""
    with open(filename) as r:
        for q in r:
            msg += q
            if search_string in q:
                msg += new_string
    with open(filename, "w") as w:
        w.write(msg)
