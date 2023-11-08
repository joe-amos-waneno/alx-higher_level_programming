#!/usr/bin/python3
"""
    Defining a student class
"""


class Student:
    """
        A class students that defines a student:
        Attributes:
            first_name (str): students first name
            last_name (str): student last name
            age (int): students age
        Methods:
            __init__ - initializes the Student instance.
            to_json - retrieves dictionary representation of Student instance.
    """
    def __init__(self, first_name, last_name, age):
        """
            Initialises the Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
            retrieve a dictionary representation of Student.
            Args:
                attr (list): attribute names to retrieve.
        """

        if attr is not None:
            res = {k: self.__dict__[k] for k in self.__dict__.keys() & attr}
            return res
        else:
            return self.__dict__
