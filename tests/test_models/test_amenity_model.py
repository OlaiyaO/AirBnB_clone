#!/usr/bin/python3

"""
    Test for the Amenity model.
"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
        Testing Amenity class
    """

    def setUp(self):
        """
        Set up a new Amenity instance for each test.
        """
        self.new_amenity = Amenity()

    def test_amenity_inheritance(self):
        """
        Test that the Amenity class inherits from BaseModel.
        """
        self.assertIsInstance(self.new_amenity, BaseModel)

    def test_amenity_attributes(self):
        """
        Test that Amenity class has the 'name' attribute.
        """
        self.assertTrue(hasattr(self.new_amenity, "name"))

    def test_amenity_attribute_type(self):
        """
        Test that Amenity class 'name' attribute's type is str.
        """
        self.assertIsInstance(self.new_amenity.name, str)


if __name__ == "__main__":
    unittest.main()
