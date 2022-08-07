#!/usr/bin/env python3


import os
import json
from msilib.schema import File


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    # @property
    # def objects(self):
    #     return self.__objects

    # @objects.setter
    # def objects(self, value):
    #     if value is not str:
    #         raise ValueError("object must be a string")
    #     else:
    #         self.__objects = value

    def all(self):
        return self.__objects

    def new(self, obj):
        # obj_data = {obj.__class__.__name__+".id": obj.id}
        # self.__objects.update(obj_data)
        obj_data = obj.to_dict()
        FileStorage.__objects[obj.__class__.__name__+"."+obj.id] = obj_data

    def save(self):
        with open(FileStorage.__file_path, "w") as x:
            json.dump(FileStorage.__objects, x)

    def reload(self):
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                FileStorage.__objects = json.load(file)
