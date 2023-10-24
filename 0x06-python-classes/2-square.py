#!/usr/bin/python3
"""Check the type"""


class Square:
    """This is a Private instance attribute: size
    Instantiation with optional """

    def __init__(self, size=0):
        """Initializing the attribute size """

        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
