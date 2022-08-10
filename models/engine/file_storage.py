#!/usr/bin/env python3
"""This module contains the methods and attributes \
    for the file storage class"""


import os
import json
from models.base_model import BaseModel
from models.user import User
from datetime import datetime


# class ObjectJSONEncoder(json.JSONEncoder):
#     def default(self, obj):
#         obj.created_at = datetime.isoformat(obj.created_at)
#         obj.updated_at = datetime.isoformat(obj.updated_at)
#         return obj.__dict__


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """this method return all the key-value pairs stored in __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """The function adds a new instance to __objects dictionary"""
        FileStorage.__objects[obj.__class__.__name__+"."+obj.id] \
            = obj

    def save(self):
        """This function unpacks the __objects dict into a json file"""
        # serialize the FileStorage.__objects into json
        temp = {}
        for key in FileStorage.__objects.keys():
            temp[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(temp, file)

    def reload(self):
        """This function unpacks the json file into the __objects dict"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as file:
                # FileStorage.__objects = json.load(file)
                # this is a dictionary
                dict_form = json.load(file)
                dict = {}
                for key in dict_form.keys():
                    split_key = key.split(".")
                    if split_key[0] == "BaseModel":
                        # this is a dict of the object
                        value = dict_form[key]
                        # create a class using the dict
                        new_class = BaseModel(**value)
                        dict[key] = new_class
                    elif split_key[0] == "User":
                        value = dict_form[key]
                        # create a class using the dict
                        new_class = User(**value)
                        dict[key] = new_class

                FileStorage.__objects = dict
