#!/usr/bin/python3
""" a function that writes an Object to a text file using JSON """


import json

def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file """
    with open('my_list.json', "w") as filename:
        json.dump(my_obj, filename)
