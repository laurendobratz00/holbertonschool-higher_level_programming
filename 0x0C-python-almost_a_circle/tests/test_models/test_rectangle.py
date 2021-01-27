#!/usr/bin/python3
import unittest

import json

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestRectangle(unittest.TestCase):

    def test_area(self):
        """ test to check area of rectangle """
        rectangle = Rectangle(1, 2)
        self.assertEqual(rectangle.area(), 2)
        rectangle2 = Rectangle(4, 4)
        self.assertEqual(rectangle2.area(), 16)
        rectangle3 = Rectangle(444, 555)
        self.assertEqual(rectangle3.area(), 246420)
        rectangle4 = Rectangle(1234567890, 9876543210)
        self.assertEqual(rectangle4.area(), 12193263111263526900)
        rectangle5 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rectangle5.area(), 2)

    def test_str(self):
        """ testing the class Rectangle """
        Base._Base__nb_objects = 0
        rectangle = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(rectangle.__str__(), "[Rectangle] (12) 2/1 - 4/6")
        rectangle2 = Rectangle(5, 5, 1)
        self.assertEqual(rectangle2.__str__(), "[Rectangle] (1) 1/0 - 5/5")

    def test_update(self):
        """ test if updated rectangle assigns an argument to each attribute """
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/1")

    def test_to_dictionary(self):
        """ check if returns dictionary representation of a Rectangle """
        Base._Base__nb_objects = 0
        r1 = Rectangle(2, 4, 1, 1, 7)
        self.assertEqual(r1.to_dictionary(), {'x': 1, 'y': 1, 'id': 7,
                                              'height': 4, 'width': 2})

if __name__ == '__main__':
    unittest.main()
