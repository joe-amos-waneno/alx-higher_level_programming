#!/usr/bin/python3
"""Module 0-lookup
Finding the list of available attributes & list of available methods of an object
"""
def lookup(obj):
    """Returns the list of the attributes and methods

    Args:    - obj: The object to look into
    """

    return dir(obj)
