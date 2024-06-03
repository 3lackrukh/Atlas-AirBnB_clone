#!/usr/bin/python3
"""Review Subclass"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class"""
    __place_id = ""
    __user_id = ""
    __text = ""

    @property
    def user_id(self):
        return self.__user_id

    @property
    def place_id(self):
        return self.__place_id

    @property
    def text(self):
        return self.__text

    @user_id.setter
    def user_id(self, value):
        self.__user_id = value

    @place_id.setter
    def place_id(self, value):
        self.__place_id = value

    @text.setter
    def text(self, value):
        self.__text = value