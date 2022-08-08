#!/usr/bin/env python3
"""This module contains the methods and attributes \
    for the file storage class"""


import os
import json


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """this method return all the key-value pairs stored in __objects"""
        return self.__objects

    def new(self, obj):
        """The function adds a new instance to __objects dictionary"""
        FileStorage.__objects[obj.__class__.__name__+"."+obj.id] \
            = obj.to_dict()

    def save(self):
        """This function unpacks the __objects dict into a json file"""
        with open(FileStorage.__file_path, "w") as x:
            json.dump(FileStorage.__objects, x)

    def reload(self):
        """This function unpacks the json file into the __objects dict"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                FileStorage.__objects = json.load(file)
