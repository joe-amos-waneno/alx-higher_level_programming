#!/usr/bin/python3
"""Module is_same_class
Finds if an object is exactly an instance of a class or not
"""

def is_same_class(obj, a_class):
    """Function to determine if obj is an instance of a_class or not

    Args:
        - obj: The object to look into
        - a_class: The class to verify the instance of obj

    Returns: True if obj is an instance of a_class
            False if obj is not an instance of a_class
    """

    return True if type(obj) is a_class else False
