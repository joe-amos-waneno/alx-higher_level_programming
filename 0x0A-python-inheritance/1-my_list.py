#!/usr/bin/python3
"""Module Mylist
Creates a class that inherits from a list class
"""

class MyList(list):
    """Class MyList inherits from a class  list"""

    def print_sorted(self):
        """Prints the list in an ascending order"""

        my_new_list = self[:]
        my_new_list.sort()
        print("{}".format(my_new_list))
