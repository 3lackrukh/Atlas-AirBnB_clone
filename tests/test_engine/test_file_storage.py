#!/usr/bin/python3
"""Tests for file storage"""
import unittest
import models
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class MyFileStorage(unittest.TestCase):
    
    def test_file_path(self):
        """Tests __file_path exists and is type str"""
        self.assertIsInstance(storage.file_path, str)

    def test_objects(self):
        """Tests __objects exists and is type dict"""
        self.assertIsInstance(storage.objects, dict)

    def test_new(self):
        """Tests to make sure objects are stored as dictionary objects"""
        obj = BaseModel()
        obj.name = 'obj'
        obj.save()
        storage.save()
        self.assertIn(obj.id, storage.__objects)

    def test_reload(self):

       