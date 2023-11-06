#!/usr/bin/python3
"""Module 9-rectangle
Creates a Rectangle class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Represents a rectangle
    Private instances attributes:
        - width
        - height
    Public method area() that
    Inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """Initializes an instance

        Args:
            - width: The width of the rectangle
            - height: The height of the rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns a formatted a string"""

        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """Computes the area of the rectangle instance and the
        Overwrites the area() method from BaseGeometry
        """

        return self.__width * self.__height
