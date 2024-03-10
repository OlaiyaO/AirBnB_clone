#!/usr/bin/python3
"""A Definition for the accessing Amenities."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Define the Amenity class.

    Attributes:
        name (str): The name given to the amenity.
    """
    name = ""
