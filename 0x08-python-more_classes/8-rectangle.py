#!/usr/bin/python3
"""
Rectangle class that calculates the area and the perimeter of a rectangle
"""

class Rectangle:
    """ Rectangle class """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ initialize the properties of the rectangle """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """This  returns set of rectangle """
        if self.__height == 0 or self.__width == 0:
            return ''
        ans = ''
        for i in range(self.__height):
            for j in range(self.__width):
                ans += str(self.print_symbol)
            ans += '\n'
        return anst[:-1]

    def __repr__(self):
        """ repr the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ delete the rectangle """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """ Getting the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Seytting the width of the rectangle """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getting the rectangle of the rectangle """
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
        """ calculates the area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ calculates the perimeter of the rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ determine the bigget rectangle and the smaller """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2
