#!/usr/bin/python3

"""
    Test for the Review model.
"""

import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """
        Testing Review class
    """

    def setUp(self):
        """
            Creates an instance for Review.
        """
        self.new_review = Review()

    def tearDown(self):
        """
            Removes the Review instance.
        """
        del self.new_review

    def test_review_inheritance(self):
        """
            Tests that the Review class Inherits from BaseModel.
        """
        self.assertIsInstance(self.new_review, BaseModel)

    def test_review_attributes_existence(self):
        """
            Test that Review class has place_id, user_id, and text
            attributes.
        """
        attributes = ["place_id", "user_id", "text"]
        for attribute in attributes:
            self.assertTrue(hasattr(self.new_review, attribute))

    def test_review_attribute_types(self):
        """
            Test that Review class attributes have the correct types.
        """
        place_id = getattr(self.new_review, "place_id")
        user_id = getattr(self.new_review, "user_id")
        text = getattr(self.new_review, "text")
        self.assertIsInstance(place_id, str)
        self.assertIsInstance(user_id, str)
        self.assertIsInstance(text, str)


if __name__ == "__main__":
    unittest.main()
