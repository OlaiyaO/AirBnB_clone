#!/usr/bin/python3
"""
    Tests for the State model.
"""

import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """
        Test the State class.
    """

    def setUp(self):
        """
            Creates an instance for State.
        """
        self.new_state = State()

    def tearDown(self):
        """
            Removes the State instance.
        """
        del self.new_state

    def test_state_inheritance(self):
        """
            Test that State class inherits from BaseModel.
        """
        self.assertIsInstance(self.new_state, BaseModel)

    def test_state_attributes_existence(self):
        """
            Test that State class contains the attribute `name`.
        """
        self.assertTrue(hasattr(self.new_state, "name"))

    def test_state_attribute_type(self):
        """
            Test that State class attribute `name` is of type str.
        """
        name = getattr(self.new_state, "name")
        self.assertIsInstance(name, str)


if __name__ == "__main__":
    unittest.main()
