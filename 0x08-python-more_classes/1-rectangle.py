#!/usr/bin/python3
"""1-rectangle, Giving the previously created rectangle properties
"""

class Rectangle:
    """the class only creates private instance attributes by
    taking in two arguments."""
    def __init__(self, width=0, height=0):
        # attribute assigned engage the setters below
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getting the width prpoperty of the triangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting the width of the rectangle"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    """Getting the height of the rectangle"""
    def height(self):
        return self.__height

    @height.setter
    """Setting the height of the rectangle"""
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = valu
