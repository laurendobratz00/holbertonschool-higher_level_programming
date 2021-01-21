#!/usr/bin/python3
""" a function that adds a new attribute to an object """


def add_attribute(obj, name, value):
    """ adds a new attribute """
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
