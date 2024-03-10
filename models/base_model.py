#!/usr/bin/python3
"""Defines BaseModel class."""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Define the BaseModel class."""

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel instance.

        Args:
            *args: Unused.
            **kwargs: Dictionary containing attribute names and values.
                - Each key is an attribute name.
                - Each value is the value of the corresponding attribute name.

        If kwargs is not empty, initialize attributes from kwargs.
        Otherwise, create id and created_at as new instance attributes.
        """
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        
        if kwargs:
            for attribute, value in kwargs.items():
                if attribute == "created_at" or attribute == "updated_at":
                    self.__dict__[attribute] = datetime.strptime(value, date_format)
                else:
                    self.__dict__[attribute] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """
        Return a string representation of the object.

        Returns:
            str: A string representation of the object, formatted as follows:
                [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__
                )

    def save(self):
        """Update the updated_at attribute and save the instance."""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance."""

        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
