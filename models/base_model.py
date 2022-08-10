#!/usr/bin/python3
"""This module contains a class called BaseModel"""


import models
import uuid
from datetime import datetime


class BaseModel:
    """ a class called basemodel used to create a basemodel """
    def __init__(self, *args, **kwargs):
        """this initialization method adds an id, and created_at attributes"""

        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

        else:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)

    def __str__(self):
        """This method overwrites the default str method"""
        return "[{}] ({}) {}"\
            .format(self.__class__.__name__, self.id, self.__dict__)

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
