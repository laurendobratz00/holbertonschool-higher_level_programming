#!/usr/bin/python3
""" class Base """


import json

class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ instantiation """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None:
            return ("[]")
        else:
            x = json.dumps(list_dictionaries)
            return x

    @classmethod
    def save_to_file(cls, list_objs):
        """ returns the JSON str representation of of list_objs to a file """
        filename = cls.__name__ + ".json"
        newobj = []
        if list_objs is not None:
            for i in list_objs:
                newobj.append(cls.to_dictionary(i))
                # ^ convert list_objs to dictionary and store it in newobj
        with open(filename, mode="w", encoding='utf-8') as a_file:
            a_file.write(cls.to_json_string(newobj))
            # convert newobj dict into json string, and write that to the file

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if json_string is None:
            return "[]"
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ class method that returns an instance """
        if cls.__name__ is "Rectangle":
            dummyobject = cls(1, 2)
        if cls.__name__ is "Square":
            dummyobject = cls(1)
        dummyobject.update(**dictionary)
        return dummyobject
