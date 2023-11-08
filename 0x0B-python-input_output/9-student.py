#!/usr/bin/python3
"""Define the class Student."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student.

        Args:
            first_name (str): first name of the student.
            last_name (str): last name of the student.
            age (int): Age of  student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Gets a dictionary representation of Student."""

        return self.__dict__
