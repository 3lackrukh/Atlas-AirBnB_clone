#!/usr/bin/python3
"""Tests for file storage"""
import unittest
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
        store1 = FileStorage()
        obj = BaseModel()
        obj2 = BaseModel()
        store1.new(obj)
        store1.new(obj2)
        self.assertIn(obj.id, store1.objects)
        self.assertIn(obj2.id, store1.objects)
