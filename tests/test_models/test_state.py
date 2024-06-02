import unittest
from models.state import State

class TestState(unittest.TestCase):

    def setUp(self):
        """Set up a new State object before each test."""
        self.state = State()

    def test_inheritance_from_BaseModel(self):
        """Test that State inherits from BaseModel."""
        self.assertIsInstance(self.state, BaseModel)

    def test_name_attribute(self):
        """Test that State has a 'name' attribute."""
        self.assertIn('name', self.state.__dict__)

    def test_name_default_value(self):
        """Test that 'name' attribute defaults to an empty string."""
        self.assertEqual(self.state.name, "")

if __name__ == "__main__":
    unittest.main()