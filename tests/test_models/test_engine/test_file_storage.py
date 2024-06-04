#!/usr/bin/python3
"""Tests for file storage"""
import unittest
import models
import os
import json
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
        self.file_path = 'file_test.json'
        self.storage = FileStorage()
        self.storage.set_file_path(self.file_path)
        self.obj = BaseModel()
    
    def tearDown(self):
        """file cleanup after testing"""
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_file_path(self):
        """Tests __file_path exists and is type str"""
        self.assertIsInstance(self.storage.file_path, str)
        self.assertFalse(os.path.exists(self.file_path))
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

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

    def test_save_reload(self):
        """Tests that save serializes object to json file
            and reload correctly deserializes object data"""
        k = f"{self.obj.__class__.__name__}.{self.obj.id}"
        self.storage.new(self.obj)
        self.storage.save()
        storage_2 = FileStorage()
        storage_2.reload()
        reloaded_obj = storage_2.all()[k]
        self.assertEqual(reloaded_obj.id, self.obj.id)
        self.assertEqual(reloaded_obj.to_dict(), self.obj.to_dict())

    if __name__ == '__main__':
        unittest.main()
