#!/usr/bin/python3
""" write a class BaseGeometry """


def area(self):
    """ area """
    raise Exception("area() is not implemented")

def integer_validator(self, name, value):
    """ public instance method """
    if type(value) is not int:
        raise TypeError("<name> must be an integer")
    if value <= 0:
        raise ValueError("<name> must be greater than 0")
