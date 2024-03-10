#!/usr/bin/python3
"""This class defines State class with it's public attributes."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents the current state.

    Attributes:
        name (str): State name.
    """
    name = ""
