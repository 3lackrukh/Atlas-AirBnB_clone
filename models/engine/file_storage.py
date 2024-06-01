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
from models.base_model import BaseModel


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
    
    def __init__(self, file_path="file.json"):
        self.__file_path = file_path
        self.__objects = {}

    @property
    def file_path(self):
        return self.__file_path

    @property
    def objects(self):
        return self.__objects

    @file_path.setter
    def file_path(self, file_path):
        self.__file_path = file_path

    @objects.setter
    def objects(self, objects):
        self.objects = objects

    def all(self):
        """Returns the dictionary objects"""
        return self.objects

    def new(self, obj):
        """Stores an object in objects"""
        self.objects[obj.id] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file specified in __file_path"""
        with open(self.file_path, "w") as f:
            json.dump(self.objects, f)

    def reload(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                data = json.load(f)
                for i in data:
                    kw = {k: v for k, v in i.items() if k!= '__class__'}
                    self.new(BaseModel(**kw))
