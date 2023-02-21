#!/usr/bin/python3
"""
JSON instantion class
"""

import json
from models.base_model import BaseModel

classes = {"BaseModel":}

class FileStorage:
    """
    serializes instances to a JSON file
    and deserializes JSON files to an instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """sets in __objects the obj with
        key <obj class name>.id"""
        if obj:
            obj_dict_key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[obj_dict_key] = obj

    def save(self):
        """
        manage serialization of objects to json
        """
        new_obj = {}

        for key, value in self.__objects.items():
            new_obj[key] = value.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(new_obj, file)

    def reload(self):
        """deserializes the JSON file to __objects"""