#!/usr/bin/python3
""" a function that creates an Object from a JSON file """


import json

def load_from_json_file(filename):
    """ a function that creates an object """
    with open(filename, mode="r", encoding='utf-8') as filename:
        return json.load(filename)
