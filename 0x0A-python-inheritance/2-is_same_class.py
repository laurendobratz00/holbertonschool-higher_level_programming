#!/usr/bin/python3
""" a function that returns True or False if the object is an instance """


def is_same_class(obj, a_class):
    """ a function that returns True or False
    """
    if a_class is not object:
        return (type(obj) == a_class)
