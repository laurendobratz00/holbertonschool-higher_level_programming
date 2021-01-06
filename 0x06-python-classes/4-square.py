#!/usr/bin/python3
""" This module demonstrates a square """


class Square:
    """ This initializes vars """

    def __init__(self, size=0):
        """ Initialize the square.
        Args:
            size(int): Private attribute for size of square.
        Return:
            None
        """
        self.__size = size

    @property
    def size(self):
        """ getter for the method """
        return(self.__size)

    @size.setter
    def size(self, value):
        """ setter for the method """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ multiplying height and width """
        return self.__size * self.__size
