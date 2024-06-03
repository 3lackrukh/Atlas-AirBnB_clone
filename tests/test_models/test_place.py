#!/usr/bin/python3
"""this file contains code for testing the Place class"""
import unittest
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class Test_Place(unittest.TestCase):
    """tests for the Place class"""
    def test_1(self):
        obj = Place()
        self.assertIsInstance(obj.name, str)
        self.assertIsInstance(obj.user_id, str)
        self.assertIsInstance(obj.city_id, str)
        self.assertIsInstance(obj.description, str)
        self.assertIsInstance(obj.price_by_night, int)
        self.assertIsInstance(obj.number_rooms, int)
        self.assertIsInstance(obj.number_bathrooms, int)
        self.assertIsInstance(obj.max_guest, int)
        self.assertIsInstance(obj.longitude, float)
        self.assertIsInstance(obj.latitude, float)
        self.assertIsInstance(obj.amenity_ids, list)
        
