#!/usr/bin/python3
"""this file contains code for testing the City class"""
import unittest
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.city import City
from models.base_model import BaseModel
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class Test_City(unittest.TestCase):
    """tests for the City class"""
    def test_1(self):
        obj = City()
        self.assertIsInstance(obj.name, str)
        self.assertIsInstance(obj.state_id, str)
