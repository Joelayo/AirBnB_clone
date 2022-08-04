#!/usr/bin/env python3
"""This module contains a class called BaseModel"""

import uuid
import datetime


class BaseModel:
    """ a class called basemodel used to create a basemodel """
    def __init__(self):
        """this initialization method adds an id, and created_at attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """This method overwrites the default str method"""
        return "[{}] ({}) {}"\
            .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """This method updates the updated attribute to the current time"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """This method adds the classname the instance"""
        classkey = {"__class__": self.__class__.__name__}
        obj_dict = self.__dict__
        obj_dict.update(classkey)
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return obj_dict
