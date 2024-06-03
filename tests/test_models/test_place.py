#!/usr/bin/python3
"""this file contains code for testing the Place class"""
import unittest
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.review import Review
from models.state import State
from models.user import User


class Test_Place(unittest.TestCase):
    """tests for the Place class"""
    def test_1(self):
        obj = State()
        assertIsInstance(obj.name, str)
        assertIsInstance(obj.user_id, str)
        assertIsInstance(obj.city_id, str)
        assertIsInstance(obj.description, str)
        assertIsInstance(obj.price_by_night, int)
        assertIsInstance(obj.number_rooms, int)
        assertIsInstance(obj.number_bathrooms, int)
        assertIsInstance(obj.max_guest, int)
        assertIsInstance(obj.longitude, int)
        assertIsInstance(obj.latitude, int)
        assertIsInstance(obj.amenity_ids, list)
        
