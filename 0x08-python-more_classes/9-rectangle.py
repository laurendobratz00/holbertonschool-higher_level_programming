#!/usr/bin/python3
""" This module contains a class Rectangle """


class Rectangle:
    """ This is a class Rectangle defined by private attr width and height.
    Attributes:
        number_of_instances: incremented during new instance and decremented
        during deletion
        __height: int
        __weight: int
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ getting width and height """
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ getter for the method """
        return(self.__width)

    @width.setter
    def width(self, value):
        """ setting the width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter for the method """
        return(self.__height)

    @height.setter
    def height(self, value):
        """ setting the height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ finding the area """
        return self.height * self.width

    def perimeter(self):
        """ finding the perimeter """
        if self.width is 0:
            return 0
        if self.height is 0:
            return 0
        return (2 * self.height) + (2 * self.width)

    def __str__(self):
        """ printing the rectangle with # """
        output = ""
        if self.width is 0:
            print()
        if self.height is 0:
            print()
        for x in range(self.height):
            for y in range(self.width):
                output += str(self.print_symbol)
            if x == self.height - 1:
                break
            else:
                output += '\n'
        return output

    def __repr__(self):
        """ returns a string representation """
        return 'Rectangle(%s, %s)' % (self.width, self.height)

    def __del__(self):
        """ prints message when an instance is deleted """
        print('Bye rectangle...')
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) == Rectangle.area(rect_2):
            return rect_1
        if Rectangle.area(rect_1) > Rectangle.area(rect_2):
            return rect_1
        if Rectangle.area(rect_2) > Rectangle.area(rect_1):
            return rect_2

    @classmethod
    def square(cls, size=0):
        my_square = Rectangle()
        my_square.width = size
        my_square.height = size
        return my_square
