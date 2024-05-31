#!/usr/bin/python3

"""
    This module defines class FileStorage which
        -  serializes an instance of BaseModel
            to a JSON file
        -  deserializes a JSON file to an
            instance of BaseModel
""" 

import json
from models.base_model import BaseModel


class FileStorage:
    """
        Attributes:
            - __file_path(str): path to the JSON file
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

    self.__file_path = ("")

    self.__objects = []

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """stores an object in __objects"""
        __objects["obj.id"] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file specified in __file_path"""
        if self.__file_path:
            for key in self.__objects:
                json.dumps(self.__objects[key])
                with open(__file_path, "w") as f:
                    f.write(self.objects[key])
            else pass