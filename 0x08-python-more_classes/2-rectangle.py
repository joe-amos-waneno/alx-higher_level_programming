#!/usr/bin/python3
"""
Rectangle class that calculates the area and peremeter
"""


class Rectangle:
    """ Rectangle Class"""
    def __init__(self, width=0, height=0):
        """ Initializ the  width and the height """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ Getting the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setting the width of the rectangle """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getting the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setting the height of the rectangle """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ calculating the area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ calculating  the perimeter of a Rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
