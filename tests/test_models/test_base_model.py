#!/usr/bin/python3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from models.base_model import BaseModel
import unittest


class testBaseModel(unittest.TestCase):
    """test Base class for models with basic methods."""

    def test_init(self):
        """Test initialization of BaseModel instances."""
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        """Test save method of BaseModel instances."""
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at

        current_updated_at = my_model.save()
        self.assertNotEqual(initial_updated_at, current_updated_at)

    def test_to_dic(self):
        """Test to_dict method of BaseModel instances."""
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)

        self.assertEqual(my_model_dict["__class__"], my_model.__class__.__name__)
        self.assertEqual(my_model_dict["id"], my_model.id)
        self.assertEqual(my_model_dict["created_at"],
                         my_model.created_at.isoformat())
        self.assertEqual(my_model_dict["updated_at"],
                         my_model.updated_at.isoformat())

    def test_str(self):
        """Test string representation of BaseModel instances."""
        my_model = BaseModel()
        self.assertTrue(str(my_model).startswith("[BaseModel]"))
        self.assertIn(my_model.id, str(my_model))
        self.assertIn(str(my_model.__dict__), str(my_model))


if __name__ == "__main__":
    unittest.main()

