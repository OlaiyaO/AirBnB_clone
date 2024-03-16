#!/usr/bin/python3

"""
    Test for the City model.
"""

import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """
        Testing City class
    """

    def setUp(self):
        """
        Set up a new City instance for each test.
        """
        self.new_city = City()

    def test_city_inheritance(self):
        """
        Test that the City class inherits from BaseModel.
        """
        self.assertIsInstance(self.new_city, BaseModel)

    def test_city_attributes(self):
        """
        Test that City class has the 'state_id' and 'name' attributes.
        """
        self.assertTrue(hasattr(self.new_city, "state_id"))
        self.assertTrue(hasattr(self.new_city, "name"))

    def test_type_name(self):
        """
        Test the type of 'name' attribute.
        """
        name = getattr(self.new_city, "name")
        self.assertIsInstance(name, str)

    def test_type_state_id(self):
        """
        Test the type of 'state_id' attribute.
        """
        state_id = getattr(self.new_city, "state_id")
        self.assertIsInstance(state_id, str)


if __name__ == "__main__":
    unittest.main()
