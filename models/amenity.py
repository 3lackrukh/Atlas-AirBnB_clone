#!/usr/bin/python3
"""Amenity Subclass"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class"""
    __name = ""

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value