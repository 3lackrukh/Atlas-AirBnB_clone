#!/usr/bin/python3
"""State Subclass"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class"""
    _name = ""

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value