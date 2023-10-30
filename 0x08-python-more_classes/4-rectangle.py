#!/usr/bin/python3
"""
Rectangle class that calculates the area and the poerimeter of a rectangle
"""


class Rectangle:
    """ Rectangle class """
    def __init__(self, width=0, height=0):
        """ initialize the rectangles property """
        self.width = width
        self.height = height

    def __str__(self):
        """ return the set of the rectangle """
        if self.__height == 0 or self.__width == 0:
            return ''
        ans = ''
        for i in range(self.__height):
            for j in range(self.__width):
                ans += '#'
            ans += '\n'
        return ans[:-1]

    def __repr__(self):
        """ The rectangles repr """
        return "Rectangle({}, {})".format(self.__width, self.__height)

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
        """ Getting the height of the rectang;le """
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
        """ calculating the perimeter of the rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
