#!/usr/bin/python3
"""Module 10-square
Creates a square class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represents a square
    Private instance attribute size
    Public method area() that
    Inherits from Rectangle
    """

    def __init__(self, size):
        """Initialize a Square

        Args:
            - size: The size of the square
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return super().__str__()

    def area(self):
        """Computes the area of a Square instance and then
        Ovewrites the area() method from Rectangle
        """

        return self.__size ** 2
