#!/usr/bin/python3
"""this file contains code for testing the State class"""
import unittest
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State


class Test_State(unittest.TestCase):
    """tests for the State class"""
    def test_1(self):
        obj = State()
        assertIsInstance(obj.name, str)
