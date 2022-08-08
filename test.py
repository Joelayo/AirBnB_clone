#!/usr/bin/env python3

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

test = BaseModel()
test2 = BaseModel()
test3 = BaseModel()
test4 = BaseModel()
storage = FileStorage()
# add to __objects
storage.new(test)

# add __objects to file.json
storage.save()

# add to __objects
storage.new(test2)
storage.new(test3)
storage.new(test4)

print(storage.all())
print("-------------------------------")
# pack from file.json into __object
storage.reload()

# show what is in __objects
print(storage.all())
# i expect to see only one
