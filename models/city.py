#!/usr/bin/python3
"""City Subclass"""
from models.base_model import BaseModel


class City (BaseModel):
    """City class"""
    _state_id = ""
    _name = ""

    @property
    def name(self):
        return self.__name

    @property
    def state_id(self):
        return self.__state_id

    @name.setter
    def name(self, value):
        self.__name = value

    @state_id.setter
    def state_id(self, value):
        self.__state_id = value