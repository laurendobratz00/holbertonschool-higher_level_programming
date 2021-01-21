#!/usr/bin/python3
""" defines rebel int class """


class MyInt(int):
""" class myint """

def __eq__(self, other):
    """ returns opposites """
    return super().__ne__(other)

def __ne__(self, other):
    """ returns opposites """
    return super().__eq__(other)
