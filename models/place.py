#!/usr/bin/python3
"""Place Subclass"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place class"""
    user_id = ""
    city_id = ""
    name = ""
    description = ""
    price_by_night = 0
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
