#!/usr/bin/python3
"""This file Defines Review class with it's public attributes."""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Defines Review class.

    Attributes:
        place_id (str): Identifier of associated place.
        user_id (str): Identifier of associated user.
        text (str): Review text.
    """
    place_id = ""
    user_id = ""
    text = ""
