#!/usr/bin/python3
"""returns the dictionary description with a simple data structure."""


def class_to_json(obj):
    """function that return a dictionary description of an object."""
    return obj.__dict__
