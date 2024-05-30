#!/usr/bin/python3
import unittest
import uuid
import datetime

from models.base_model import BaseModel

class TestMyClass(unittest.TestCase):

    def setUp(self):
        obj = BaseModel()

    def tearDown(self):
        del obj

    def test_id_initialization(self):
        self.assertIsNotNone(self.obj.id, "The id should not be None")
        self.assertIsInstance(self.obj.id, str)

    def test_created_at(self):
        self.assertIsNotNone(self.obj.created_at)
        

if __name__ == '__main__':
    unittest.main()