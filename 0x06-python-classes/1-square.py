#!/usr/bin/python3
""" This is a square defined with a private instance attribute size
"""


class Square:
    """ A square defined by private instance attribute and insta    ntiation
    """
    name = "Square"

    def __init__(self, size):
        self.__size = size
