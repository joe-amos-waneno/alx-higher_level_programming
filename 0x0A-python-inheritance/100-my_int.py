#!/usr/bin/python3
"""Module 100-my_int
Creates a class that inherits from int
"""

class MyInt(int):
    """Class inheriting from int but reverses the behaviour of != and ==
    """

    def __eq__(self, other):
        """Equality changes to inequality"""

        return super().__ne__(other)

    def __ne__(self, other):
        """Inequality changes to equality"""

        return super().__eq__(other)
