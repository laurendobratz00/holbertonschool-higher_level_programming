#!/usr/bin/python3
""" a class Rectangle that inherits from BaseGeometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class rectangle """
    def __init__(self, width, height):
        """ initializes rectangle """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str(self):
        """ str repr of Rectangle """
        str_rep = "[Rectangle]" + str(self.width) + "/" + str(self.__height)
        return str_rep

    def area(self):
        """ area """
        return (self.__width * self.__height)
