import unittest
from models.state import State

class TestState(unittest.TestCase):

    def setUp(self):
        """Set up a common State instance for each test."""
        self.state = State()

    def test_init(self):
        """Test State initialization."""
        self.assertIsInstance(self.state, State)
        self.assertEqual(self.state.name, "")

    def test_inheritance_from_BaseModel(self):
        """Test inheritance from BaseModel."""
        self.assertIsInstance(self.state, BaseModel)
        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))

if __name__ == "__main__":
    unittest.main()