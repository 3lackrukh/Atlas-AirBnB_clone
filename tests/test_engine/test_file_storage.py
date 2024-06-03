#!/usr/bin/python3
"""Tests for file storage"""
import unittest
import models
import os
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


class TestFileStorage(unittest.TestCase):
    
    def setUp(self):
        """set up for testing"""
        self.storage = FileStorage()
        self.storage.set_file_path("file_test.json")
        self.obj = BaseModel()
        self.storage.new(self.obj)
    
    #def tearDown(self):
     #   """memory cleanup after testing"""
      #  try:
       #     os.remove(self.file_path)
        #except FileNotFoundError:
         #   pass

    def test_file_path(self):
        """Tests __file_path exists and is type str"""
        self.assertIsInstance(self.storage.file_path, str)

    def test_objects(self):
        """Tests __objects exists and is type dict"""
        self.assertIsInstance(self.storage.objects, dict)

    def test_new(self):
        """Tests to make sure objects are stored as dictionary objects"""
        k = f"{self.obj.__class__.__name__}.{self.obj.id}"
        self.storage.new(self.obj)
        self.assertIn(k, self.storage.all())

    def test_all(self):
        """tests the all method"""
        k = f"{self.obj.__class__.__name__}.{self.obj.id}"
        self.storage.new(self.obj)
        objs = self.storage.all()
        self.assertEqual(objs[k], self.obj)

    #def test_reload(self):       