#!/usr/bin/python3
"""Module for Base class
Contains the Base class for the AirBnB clone console.
"""

import uuid
from datetime import datetime
import models


class BaseModel:

    """Class for base model of object hierarchy."""

    def __init__(self, *args, **kwargs):
        """Initialization of a Base instance.
        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

    def __str__(self):
        """Returns a human-readable string representation
        of an instance."""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """This method updates the updated attribute to the current time"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """This method adds the classname as a key to the instance """
        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = datetime.isoformat(self.created_at)
        obj_dict["updated_at"] = datetime.isoformat(self.updated_at)
        obj_dict["__class__"]: self.__class__.__name__
        return obj_dict
