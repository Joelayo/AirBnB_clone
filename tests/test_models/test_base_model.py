#!/usr/bin/env python3
"""A test for base model"""
from __future__ import with_statement
from datetime import datetime
import unittest
# from models.base_model import BaseModel
# import models.base_model
from models import base_model
BaseModel = base_model.BaseModel


class TestBaseModel(unittest.TestCase):
    """a class called testbasemodel"""

    def test_modelDocString(self):
        self.assertTrue(len(base_model.__doc__) >= 1)

    def test_classDocString(self):
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_str(self):
        testInstance = BaseModel()
        self.assertEqual(print(testInstance), print("[BaseModel] ({}) {}"
                                                    .format(testInstance.id,
                                                            testInstance
                                                            .__dict__)))

    def test_id(self):
        testInstance = BaseModel()
        self.assertTrue(len(testInstance.id) >= 1)

    def test_created_at(self):
        testInstance = BaseModel()
        self.assertTrue(testInstance.created_at)

    def test_updated_at(self):
        testInstance = BaseModel()
        self.assertTrue(testInstance.updated_at)

    # def test_save(self):
    #     testInstance = BaseModel()
    #     testInstance.name = 'My second model'
    #     testInstance.save()
    #     self.assertNotEqual(testInstance.created_at,
    #                         testInstance.updated_at)


if __name__ == "__main__":
    unittest.main()
