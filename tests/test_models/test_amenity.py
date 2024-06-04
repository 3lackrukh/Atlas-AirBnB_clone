#!/usr/bin/python3
"""this file contains code for testing the Amenity class"""
import unittest
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class Test_Amenity(unittest.TestCase):
    """tests for the Amenity class"""
    def test_1(self):
        obj = Amenity()
        self.assertIsInstance(obj.name, str)
    # self is the instance of the test case class
    # assertIsInstance is the method from TestCase, and checks whether an object is and instance of the class
    # obj.name accesses the NAME attribute of the object OBJ
    # str is the type being checked, in this case, a string
    # So, self.assertIsInstance(obj.name, str) checks whether the name attribute of obj is an instance of the 
    #str class (i.e., whether it is a string). If obj.name is not a string, the test will fail, and an 
    #assertion error will be raised
