#!/usr/bin/python3
"""User Subclass"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    @property
    def email(self):
        return self.__email

    @property
    def password(self):
        return self.__password

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @email.setter
    def email(self, value):
        self.__email = value

    @password.setter
    def password(self, value):
        self.__password = value

    @first_name.setter
    def first_name(self,value):
        self.__first_name = value

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value