#!/usr/bin/python3
""" This function returns true if the object is an instance of inherited class
"""


def inherits_from(obj, a_class):
    """ Returns true if the object is an instance of inherited class """

    return (issubclass(type(obj), a_class) and type(obj) != a_class)
