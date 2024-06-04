#!/usr/bin/python3
import unittest
import uuid
import datetime

from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_id_initialization(self):
        obj = BaseModel()
        self.assertIsNotNone(obj.id)
        self.assertIsInstance(obj.id, str)

    def test_created_at(self):
        obj = BaseModel()
        self.assertIsNotNone(obj.created_at)
        self.assertTrue(isinstance(obj.created_at, datetime.datetime))

    def test_updated_at(self):
        obj = BaseModel()
        self.assertIsNotNone(obj.updated_at)
        self.assertTrue(isinstance(obj.updated_at, datetime.datetime))
    
    def test_str(self):
        obj = BaseModel()
        expected = "[{}] ({}) {}".format(
            obj.__class__.__name__,
            obj.id,
            obj.__dict__)
        self.assertEqual(expected, str(obj))

    def test_save(self):
        obj = BaseModel()
        pre_save = obj.updated_at
        obj.save()
        post_save = obj.updated_at
        self.assertNotEqual(pre_save, post_save)
    
    def test_to_dict(self):
        obj = BaseModel()
        dictionary = obj.to_dict()
        self.assertEqual(dictionary["__class__"], "BaseModel")
        self.assertEqual(dictionary["id"], obj.id)
        self.assertEqual(dictionary["created_at"], obj.created_at.isoformat())
        self.assertEqual(dictionary["updated_at"], obj.updated_at.isoformat())

    def test_init_from_dict(self):
        obj = BaseModel()
        obj_2 = BaseModel()
        self.assertNotEqual(obj.id, obj_2.id)
        json_obj = BaseModel(**obj.to_dict())
        self.assertEqual(obj.id, json_obj.id)
        self.assertEqual(obj.created_at, json_obj.created_at)
        self.assertEqual(obj.updated_at, json_obj.updated_at)

if __name__ == '__main__':
    unittest.main()
