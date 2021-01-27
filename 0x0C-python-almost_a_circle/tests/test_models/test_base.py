#!/usr/bin/python3
""" test cases for Base """
import unittest

import json

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    """ class TestBase """

    def test_to_json_string(self):
        """ Test conv to json str in to_json_string method
        """
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertTrue(type(Base.to_json_string(None)), str)
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertTrue(type(Base.to_json_string([])), str)
        myDict = {'id': 4, 'width': 3, 'height': 4, 'x': 1, 'y': 3}
        myDict2 = {'id': 3, 'width': 6, 'height': 2, 'x': 1, 'y': 9}
        jsonized = Base.to_json_string([myDict, myDict2])
        self.assertTrue(type(jsonized) is str)
        myDict3 = json.loads(jsonized)
        self.assertEqual(myDict3, [myDict, myDict2])

    def test_from_json_string(self):
        """ Test conversion from json str in from_json_string method
        """
        string = '[{"id": 4, "width": 3, "height": 4, "x": 1, "y": 3}, {"id": 3, "width": 6, "height": 2, "x": 1, "y": 9}]'
        jsonized = Base.from_json_string(string)
        self.assertEqual(len(jsonized), 2)
        self.assertTrue(type(Base.from_json_string(None)), str)
        self.assertEqual(Base.from_json_string(None), "[]")
        self.assertTrue(type(jsonized) is list)

    def test_create_rect(self):
        """ Test that returns the list of the JSON str representation """
        rect1 = Rectangle(1, 2, 3)
        rect1_dict = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dict)
        self.assertNotEqual(rect1, rect2)

    def test_create_square(self):
        """ Test that creates square object """
        square1 = Square(5, 5, 5, 4)
        square1_dict = square1.to_dictionary()
        square2 = Square.create(**square1_dict)
        self.assertNotEqual(square1, square2)

    def test_loads_from_rect(self):
        """ test that file loads from rect obj """
        rect1 = Rectangle(1, 2, 3)
        rect2 = Rectangle(1, 2)
        listofrects = [rect1, rect2]
        Rectangle.save_to_file(listofrects)
        listofrects2 = Rectangle.load_from_file()
        self.assertNotEqual(listofrects, listofrects2)

    def test_loads_from_square(self):
        """ test that file loads from square obj """
        square1 = Square(2, 2, 3)
        square2 = Square(2, 2)
        listofsquares = [square1, square2]
        Square.save_to_file(listofsquares)
        listofsquares2 = Square.load_from_file()
        self.assertNotEqual(listofsquares, listofsquares2)

if __name__ == '__main__':
    unittest.main()
