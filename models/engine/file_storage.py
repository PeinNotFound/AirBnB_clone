import json
import os
from models.base_model import BaseModel


class FileStorage:
    '''Handles storage of objects in a JSON file.'''
    __file_path = "file.json"
    __objects = {}

    def new(self,obj):
        '''Return a dictionary of all stored objects.'''
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name.id)
        FileStorage.__objects[key] = obj


    def all(self):
        '''Add a new object to the storage.'''
        return FileStorage.__objects


    def save(self):
        '''Serialize and saves all objects to the JSON file.'''
        all_objs = FileStorage.__objects
        obj_dict = {}
        for obj in all_objs.keys():
            obj_dict[obj] = all_objs[obj.to_dict()]

        with open(FileStorage.__file_path, "w", encoding="utf-8") as json_file:
            json.dump(obj_dict, json_file)


    def reload(self):
        '''Load objects from the JSON file into the storage.'''
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as json_file:
                try:
                    obj_dict = json.load(json_file)

                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')

                        cls = eval(class_name)
                        instance = cls(**value)
                        FileStorage.__objects[key] = instance

                except Exception:
                    pass
