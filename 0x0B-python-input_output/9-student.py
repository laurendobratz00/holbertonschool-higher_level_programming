#!/usr/bin/python3
"""  """



class Student:
    """ """
    def __init__(self, first_name, last_name, age):
        """ """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ """
        if attrs is None or type(attrs) is not list
            return self.__dict__
        else:
            n = {}
            for x in self.__dict__:
                for y in attrs:
                    if x is y:
                        n[x] = self.__dict__[x]
            return n
