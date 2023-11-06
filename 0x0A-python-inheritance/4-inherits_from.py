#!/usr/bin/python3
"""Module inherits_from
Finds if the object is an instance of a class that inherited from the specified class"""


def inherits_from(obj, a_class):
    """Determines if obj is an instance of a class that
    inherited from the a_class

    Args:
        - obj: The object to be looked
        - a_class: The class to be evaluated

    Returns: True or False
    """

    return isinstance(obj, a_class) and type(obj) != a_class
