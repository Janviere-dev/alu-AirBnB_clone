#!/usr/bin/python3
"""Unit tests for BaseModel."""

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Tests for the BaseModel class."""

    def test_instance_creation(self):
        """Test if BaseModel instance is created."""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_to_dict_returns_dict(self):
        """Test if to_dict returns a dictionary."""
        obj = BaseModel()
        self.assertIsInstance(obj.to_dict(), dict)
