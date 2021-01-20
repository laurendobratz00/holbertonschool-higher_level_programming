#!/usr/bin/python3
""" Class MyList that inherits from list
"""


class MyList(list):
    """ A class MyList that prints a sorted list
    """

    def print_sorted(self):
        """ This method has a public instance and prints a sorted list
        """

        print(sorted(self))
