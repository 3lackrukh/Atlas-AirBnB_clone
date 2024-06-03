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
