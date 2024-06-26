#!/usr/bin/python3
"""this file contains code for testing the Review class"""
import unittest
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class Test_Review(unittest.TestCase):
    """tests for the Review class"""
    def test_1(self):
        obj = Review()
        self.assertIsInstance(obj.place_id, str)
        self.assertIsInstance(obj.user_id, str)
        self.assertIsInstance(obj.text, str)
