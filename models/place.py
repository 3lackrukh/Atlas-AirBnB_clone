#!/usr/bin/python3
"""Place Subclass"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place class"""
    user_id = ""
    city_id = ""
    name = ""
    description = ""
    price = 0
    number_of_rooms = 0
    number_of_bathrooms = 0
    amenities = []
    