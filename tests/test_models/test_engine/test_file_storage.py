#!/usr/bin/python3
'''Module for FilStorage unittest'''

import os
import json
import AirBnB_clone.models
import unittest
from AirBnB_clone.models.base_model import BaseModel
from AirBnB_clone.models.engine.file_storage import FileStorage
from AirBnB_clone.models.user import User
from AirBnB_clone.models.state import State
from AirBnB_clone.models.place import Place
from AirBnB_clone.models.city import City
from AirBnB_clone.models.amenity import Amenity
from AirBnB_clone.models.review import Review


class TestFileStorage_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the FileStorage class.
    """

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(AirBnB_clone.models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """
    Unittests for testing methods of the FileStorage class.
    """

    def setUp(self):
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(AirBnB_clone.models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            AirBnB_clone.models.storage.all(None)

    def test_new(self):
        my_base_model = BaseModel()
        my_user = User()
        my_state = State()
        my_place = Place()
        my_city = City()
        my_amenity = Amenity()
        my_review = Review()
        AirBnB_clone.models.storage.new(my_base_model)
        AirBnB_clone.models.storage.new(my_user)
        AirBnB_clone.models.storage.new(my_state)
        AirBnB_clone.models.storage.new(my_place)
        AirBnB_clone.models.storage.new(my_city)
        AirBnB_clone.models.storage.new(my_amenity)
        AirBnB_clone.models.storage.new(my_review)
        self.assertIn("BaseModel." + my_base_model.id, AirBnB_clone.models.storage.all().keys())
        self.assertIn(my_base_model, AirBnB_clone.models.storage.all().values())
        self.assertIn("User." + my_user.id, AirBnB_clone.models.storage.all().keys())
        self.assertIn(my_user, AirBnB_clone.models.storage.all().values())
        self.assertIn("State." + my_state.id, AirBnB_clone.models.storage.all().keys())
        self.assertIn(my_state, AirBnB_clone.models.storage.all().values())
        self.assertIn("Place." + my_place.id, AirBnB_clone.models.storage.all().keys())
        self.assertIn(my_place, AirBnB_clone.models.storage.all().values())
        self.assertIn("City." + my_city.id, AirBnB_clone.models.storage.all().keys())
        self.assertIn(my_city, AirBnB_clone.models.storage.all().values())
        self.assertIn("Amenity." + my_amenity.id, AirBnB_clone.models.storage.all().keys())
        self.assertIn(my_amenity, AirBnB_clone.models.storage.all().values())
        self.assertIn("Review." + my_review.id, AirBnB_clone.models.storage.all().keys())
        self.assertIn(my_review, AirBnB_clone.models.storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            AirBnB_clone.models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            AirBnB_clone.models.storage.new(None)

    def test_save(self):
        my_base_model = BaseModel()
        my_user = User()
        my_state = State()
        my_place = Place()
        my_city = City()
        my_amenity = Amenity()
        my_review = Review()
        AirBnB_clone.models.storage.new(my_base_model)
        AirBnB_clone.models.storage.new(my_user)
        AirBnB_clone.models.storage.new(my_state)
        AirBnB_clone.models.storage.new(my_place)
        AirBnB_clone.models.storage.new(my_city)
        AirBnB_clone.models.storage.new(my_amenity)
        AirBnB_clone.models.storage.new(my_review)
        AirBnB_clone.models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + my_base_model.id, save_text)
            self.assertIn("User." + my_user.id, save_text)
            self.assertIn("State." + my_state.id, save_text)
            self.assertIn("Place." + my_place.id, save_text)
            self.assertIn("City." + my_city.id, save_text)
            self.assertIn("Amenity." + my_amenity.id, save_text)
            self.assertIn("Review." + my_review.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            AirBnB_clone.models.storage.save(None)

    def test_reload(self):
        my_base_model = BaseModel()
        my_user = User()
        my_state = State()
        my_place = Place()
        my_city = City()
        my_amenity = Amenity()
        my_review = Review()
        AirBnB_clone.models.storage.new(my_base_model)
        AirBnB_clone.models.storage.new(my_user)
        AirBnB_clone.models.storage.new(my_state)
        AirBnB_clone.models.storage.new(my_place)
        AirBnB_clone.models.storage.new(my_city)
        AirBnB_clone.models.storage.new(my_amenity)
        AirBnB_clone.models.storage.new(my_review)
        AirBnB_clone.models.storage.save()
        AirBnB_clone.models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + my_base_model.id, objs)
        self.assertIn("User." + my_user.id, objs)
        self.assertIn("State." + my_state.id, objs)
        self.assertIn("Place." + my_place.id, objs)
        self.assertIn("City." + my_city.id, objs)
        self.assertIn("Amenity." + my_amenity.id, objs)
        self.assertIn("Review." + my_review.id, objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            AirBnB_clone.models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
