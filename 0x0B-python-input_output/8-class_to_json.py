#!/usr/bin/python3
""" returns dict description """


import json


def class_to_json(obj):
    """ returns dict description """
    return (obj.__dict__)
