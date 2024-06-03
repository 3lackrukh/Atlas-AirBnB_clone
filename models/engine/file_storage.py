#!/usr/bin/python3

"""
    This module defines class FileStorage which
        -  serializes an instance of BaseModel
            to a JSON file
        -  deserializes a JSON file to an
            instance of BaseModel
"""

import json
import os
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {
    "Amenity": Amenity, 
    "BaseModel": BaseModel, 
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User}


class FileStorage:
    """
        Attributes:
            - __file_path(str): path to the JSON file
                                If none is specified, defaults to 'file.json'
            - __objects(dict): objects stored by <class name>.id

        Methods:
            - all: returns the __objects dictionary
            - new: stores an object in __objects
            - save: serializes __objects to the JSON file
                    specified in __file_path
            - reload: deserializes the JSON file specified
                      in __file_path. If file does not exist,
                      does nothing.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary objects"""
        return self.__objects

    def new(self, obj):
        """Stores an object in objects"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file specified in __file_path"""
        obj_dict = {}
        for k, v in self.__objects.items():
            obj_dict[k] = v.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for k, v in json.load(f).items():
                    self.__objects[k] = (classes[v.get('__class__')](**v))
