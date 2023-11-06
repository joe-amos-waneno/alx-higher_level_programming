#!/usr/bin/python3
"""Module is_kind_of_class
Finds if the object is an instance of a class or if object is an
instance of a class that inherited from a specified class
"""

def is_kind_of_class(obj, a_class):
    """Finds out if obj is an instance of a_class or if a class
    inherited from a_class

    Args:
        - obj: The object to look into
        - a_class: The class to be evaluated

    Returns: True or False
    """

    return isinstance(obj, a_class)
