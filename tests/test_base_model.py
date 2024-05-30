#!/usr/bin/python3
import unittest
import uuid

from models.base_model import BaseModel

class TestMyClass(unittest.TestCase):
    def test_id_initialization(self):
        obj = BaseModel()
        self.assertIsNotNone(obj.id, "The id should not be None")
        self.assertIsInstance(obj.id, uuid.UUID, "The id should be an instance of uuid.UUID")
        self.assertIsInstance(obj.id, str)

if __name__ == '__main__':
    unittest.main()