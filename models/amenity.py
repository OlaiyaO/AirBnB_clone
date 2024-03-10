#!/usr/bin/python3
"""Defines Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Define the Amenity class.

    Attributes:
        name (str): The name given to the amenity.
    """
    name = ""
