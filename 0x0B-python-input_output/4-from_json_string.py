#!/usr/bin/python3
""" a function that returns an object represented by a string """


import json


def from_json_string(my_str):
    """ returns an object represented by a string """
    return (json.loads(my_str))
