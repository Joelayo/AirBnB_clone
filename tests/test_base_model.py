#!/usr/bin/env python3
"""A test for base model"""
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
        self.assertEqual(str())


if __name__ == "__main__":
    unittest.main()
