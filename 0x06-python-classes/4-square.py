#!/usr/bin/python3
""" This module demonstrates a square """


class Square:
    """ This initializes vars """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, val):

        if type(val) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
