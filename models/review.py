#!/usr/bin/python3
"""models/review inherits from the class BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review that and its instances"""
    place_id = ""
    user_id = ""
    text = ""
