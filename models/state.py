#!/usr/bin/python3
"""State Subclass"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class"""
    __name = ""

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value