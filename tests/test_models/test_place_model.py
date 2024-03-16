#!/usr/bin/python3
"""
    Test for the Place model.
"""

import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """
        Testing Place class
    """

    def setUp(self):
        """
            Creates an instance for Place.
        """
        self.new_place = Place()

    def tearDown(self):
        """
            Removes the Place instance.
        """
        del self.new_place

    def test_place_inheritance(self):
        """
            Tests that the Place class Inherits from BaseModel.
        """
        self.assertIsInstance(self.new_place, BaseModel)

    def test_place_attributes(self):
        """
            Checks that the attributes exist.
        """
        attributes = ["city_id", "user_id", "description", "name",
                      "number_rooms", "max_guest", "price_by_night",
                      "latitude", "longitude", "amenity_ids"]
        for attribute in attributes:
            self.assertTrue(hasattr(self.new_place, attribute))

    def test_type_amenity(self):
        """
            Test the type of amenity_ids.
        """
        amenity = getattr(self.new_place, "amenity_ids")
        self.assertIsInstance(amenity, list)

    def test_type_longitude(self):
        """
            Test the type of longitude.
        """
        longitude = getattr(self.new_place, "longitude")
        self.assertIsInstance(longitude, float)

    def test_type_latitude(self):
        """
            Test the type of latitude.
        """
        latitude = getattr(self.new_place, "latitude")
        self.assertIsInstance(latitude, float)

    def test_type_price_by_night(self):
        """
            Test the type of price_by_night.
        """
        price_by_night = getattr(self.new_place, "price_by_night")
        self.assertIsInstance(price_by_night, int)

    def test_type_max_guest(self):
        """
            Test the type of max_guest.
        """
        max_guest = getattr(self.new_place, "max_guest")
        self.assertIsInstance(max_guest, int)

    def test_type_number_bathrooms(self):
        """
            Test the type of number_bathrooms.
        """
        number_bathrooms = getattr(self.new_place, "number_bathrooms")
        self.assertIsInstance(number_bathrooms, int)

    def test_type_number_rooms(self):
        """
            Test the type of number_rooms.
        """
        number_rooms = getattr(self.new_place, "number_rooms")
        self.assertIsInstance(number_rooms, int)

    def test_type_description(self):
        """
            Test the type of description.
        """
        description = getattr(self.new_place, "description")
        self.assertIsInstance(description, str)

    def test_type_name(self):
        """
            Test the type of name.
        """
        name = getattr(self.new_place, "name")
        self.assertIsInstance(name, str)

    def test_type_user_id(self):
        """
            Test the type of user_id.
        """
        user_id = getattr(self.new_place, "user_id")
        self.assertIsInstance(user_id, str)

    def test_type_city_id(self):
        """
            Test the type of city_id.
        """
        city_id = getattr(self.new_place, "city_id")
        self.assertIsInstance(city_id, str)


if __name__ == "__main__":
    unittest.main()
