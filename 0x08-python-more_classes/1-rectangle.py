#!/usr/bin/python3
"""1-rectangle, Giving the previously created rectangle properties
"""
class Rectangle:
    """ Rectangle class """
    def __init__(self, width=0, height=0):
        """ Initialize the width and the height """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ Getting the width of the rectangele """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setting the width of the rectangele """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getting the height of the rectangele """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setting the height of the rectangele """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
