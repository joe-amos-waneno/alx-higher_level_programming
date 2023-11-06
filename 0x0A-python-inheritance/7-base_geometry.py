#!/usr/bin/python3
"""Module base_Geometry
Creates a BaseGeometry class
"""

class BaseGeometry:
    """A class with public instance methods"""

    def area(self):
        """Raises an Exception with a message that says
        'area() is not implemented'
        """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates the value: value"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
