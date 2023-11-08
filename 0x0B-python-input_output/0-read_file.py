#!/usr/bin/python3
"""reads the text file."""


def read_file(filename=""):
    """prints out the read file content to stdout"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
