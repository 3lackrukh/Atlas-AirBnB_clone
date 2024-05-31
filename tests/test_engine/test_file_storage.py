#!/usr/bin/python3
"""Tests for file storage"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class MyTestClass(unittest.TestCase):
    def setUp(self):
        """SetUp of a file storage instance for each test"""
        store1 = FileStorage()
    
    def test_init(self):
        """Initializes test case FileStorage"""
        self.assertIsInstance(store1.__file_path, str)
        self.assertIsInstance(store1.__objects, dict)