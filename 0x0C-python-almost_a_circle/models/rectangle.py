#!/usr/bin/python3
""" class Rectangle that inherits from Base """


from models.base import Base

class Rectangle(Base):
    """ class Rectangle that inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ instantiation """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter for the method """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ setting the width """
        self.__width = value

    @property
    def height(self):
        """ getter for the method """
        return(self.__height)

    @height.setter
    def height(self, value):
        """ setting the height """
        self.__height = value
