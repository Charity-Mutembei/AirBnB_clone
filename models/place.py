#!/usr/bin/python3
"""[models/place module] inherits from the class BaseModel"""
from models.base_model import BaseModel


class Place(BaseModel):
    """class place that has a number of attributes """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
