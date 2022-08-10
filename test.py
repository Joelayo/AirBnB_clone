#!/usr/bin/env python3

from models.base_model import BaseModel
# from models.engine.file_storage import FileStorage
from models import storage
print(storage.all())

# store = FileStorage()
test1 = BaseModel()
# my_model = BaseModel()
test1.name = "My_First_Model"
# my_model.my_number = 89
# test1.save()
print(test1)
# storage.new(test1)
# store.new(test1)
# # print(store.all())
# test2 = BaseModel()
# test3 = BaseModel()
# test4 = BaseModel()
# store.new(test2)
# store.new(test3)
# store.new(test4)
# test1.name = "testModel"
storage.save()
# print(store.all())

print("==========")
storage.reload()
print(storage.all())
