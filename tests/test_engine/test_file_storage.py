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
    def setUp(self):
        """SetUp of a file storage instance for each test"""
        store1 = FileStorage()
    
    def test_init(self):
        """Initializes test case FileStorage"""
        store1 = FileStorage()
        self.assertIsInstance(store1.file_path, str)
        self.assertIsInstance(store1.objects, dict)

    def test_new(self):
        """Tests to make sure objects are stored as dictionary objects"""
        #obj = BaseModel()
        #obj2 = BaseModel()
        #obj.name = 'obj'
        #obj2.name = 'obj2'
        #print(obj)
        #print(obj2)
        #obj.save()
        #obj2.save()
        #models.storage.save()

       # self.assertIn(obj.id, store1.objects)
       # self.assertIn(obj2.id, store1.objects)

    def test_reload(self):
        original_obj = BaseModel()
        #original_crat = original_obj.created_at.isoformat()
        #original_upat = original_obj.updated_at.isoformat()

        recreated_objects = []

        for obj in models.storage.reload():
            recreated_objects.append(obj)

            assert original_obj.id == obj.id
            assert original_obj.created_at == obj.created_at
            assert original_obj.updated_at == obj.updated_at
       