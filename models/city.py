#!/usr/bin/python3
"""This file Defines City class with its public attributes."""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Defines City class.

    Attributes:
        state_id (str): Identifier of associated state.
        name (str): City name.
    """
    state_id = ""
    name = ""
