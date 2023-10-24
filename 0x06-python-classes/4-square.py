#!/usr/bin/python3
"""Access and update the  private attribute"""


class Square:
    """Private instance attribute: size
    Instantiation with area method """

    def __init__(self, size=0):
        """Initializing attribute size """
        self.__size = size

    def area(self):
        """Calculates the  area of square"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Setting of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Initializing the  attribute size """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
