#!/usr/bin/python3
from .base_model import BaseModel
"""
This class takes from BaseModel class
"""


class Place(BaseModel):
    """
    Takes public attributes to be; city_id,
    user_id, name, description, number_rooms,
    number_bathrooms, max_guest, price_by_night,
    latitude, longitude, amenity_ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = ""
    price_by_night = ""
    latitude = ""
    longitude = ""
    amenity_ids = ""
