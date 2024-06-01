#!/usr/bin/python3
"""Unittest for User"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        """Common user instance for each test"""
        self.user = User()

    def test_init(self):
        """Tests User initialization"""
        self.assertIsInstance(self.user, User)
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_save(self):
        """Test save method indirectly by checking attribute changes."""
        self.user.save()
        self.assertIsNotNone(self.user.updated_at)

if __name__ == "__main__":
    unittest.main()