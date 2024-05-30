#!/usr/bin/python3
import unittest
import uuid
import datetime

from models.base_model import BaseModel

class TestMyClass(unittest.TestCase):

    def test_id_initialization(self):
        obj = BaseModel()
        self.assertIsNotNone(obj.id)
        self.assertIsInstance(obj.id, str)

    def test_created_at(self):
        obj = BaseModel
        self.assertIsNotNone(obj.created_at)
        

if __name__ == '__main__':
    unittest.main()