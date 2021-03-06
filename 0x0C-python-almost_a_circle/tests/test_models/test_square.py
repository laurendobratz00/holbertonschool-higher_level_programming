#!/usr/bin/python3
""" test cases for Square """
import unittest

import json

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquare(unittest.TestCase):
    """ class TestSquare """
    def test_str(self):
        """ testing the class Square """
        Base._Base__nb_objects = 0
        square = Square(5)
        self.assertEqual(square.__str__(), "[Square] (1) 0/0 - 5")
        square2 = Square(2, 2)
        self.assertEqual(square2.__str__(), "[Square] (2) 2/0 - 2")
        square3 = Square(3, 1, 3)
        self.assertEqual(square3.__str__(), "[Square] (3) 1/3 - 3")

    def test_update(self):
        """ test if updated square assigns an argument to each attribute """
        Base._Base__nb_objects = 0
        s1 = Square(5)
        s1.update(size=10)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 10")

    def test_to_dictionary(self):
        """ check if returns dictionary representation of a Square """
        Base._Base__nb_objects = 0
        s1 = Square(4, 1, 1, 7)
        self.assertEqual(s1.to_dictionary(), {'x': 1, 'y': 1, 'id': 7,
                                              'size': 4})

if __name__ == '__main__':
    unittest.main()
