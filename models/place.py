#!/usr/bin/python3
"""Place Subclass"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place class"""
    __user_id = ""
    __city_id = ""
    __name = ""
    __description = ""
    __price_by_night = 0
    __number_rooms = 0
    __number_bathrooms = 0
    __max_guest = 0
    __latitude = 0.0
    __longitude = 0.0
    __amenity_ids = []

    @property
    def user_id(self):
        return self.__user_id

    @property
    def name(self):
        return self.__name

    @property
    def city_id(self):
        return self.__city_id

    @property
    def decsription(self):
        return self.__description

    @property
    def number_rooms(self):
        return self.__number_rooms

    @property
    def number_bathrooms(self):
        return self.__number_bathrooms

    @property
    def max_guest(self):
        return self.__max_guest

    @property
    def price_by_night(self):
        return self.__price_by_night

    @property
    def latitude(self):
        return self.__latitude

    @property
    def longitude(self):
        return self.__longitude

    @user_id.setter
    def user_id(self, value):
        self.__user_id = value

    @name.setter
    def name(self, value):
        self.__name = value

    @city_id.setter
    def city_id(self, value):
        self.__city_id = value

    @decsription.setter
    def decsription(self, value):
        self.__decsription = value

    @number_rooms.setter
    def number_rooms(self, value):
        self.__number_rooms = value

    @number_bathrooms.setter
    def number_bathrooms(self, value):
        self.__number_bathrooms = value

    @max_guest.setter
    def max_guest(self, value):
        self.__max_guest = value

    @price_by_night.setter
    def price_by_night(self, value):
        self.__price_by_night = value

    @latitude.setter
    def latitude(self, value):
        self.__latitude = value

    @longitude.setter
    def longitude(self, value):
        self.__longitude = value