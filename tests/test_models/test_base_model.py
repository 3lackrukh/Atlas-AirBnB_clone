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
        obj = BaseModel()
        self.assertIsNotNone(obj.created_at)

    def test_updated_at(self):
        obj = BaseModel()
        self.assertIsNotNone(obj.updated_at)
    
    def test_str(self):
        obj = BaseModel()
        expected = "[{}] ({}) {}".format(
            obj.__class__.__name__,
            obj.id,
            obj.__dict__)
        self.assertEqual(expected, str(obj))

    def test_save(self):
        obj = BaseModel()
        initial = obj.updated_at
        obj.save()
        saved = obj.updated_at
        self.assertNotEqual(initial, saved)
    
    def test_to_dict(self):
        obj = BaseModel()
        dictionary = obj.to_dict()
        self.assertEqual(dictionary["__class__"], "BaseModel")
        self.assertEqual(dictionary["id"], obj.id)
        self.assertEqual(dictionary["created_at"], obj.created_at.isoformat())
        self.assertEqual(dictionary["updated_at"], obj.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()