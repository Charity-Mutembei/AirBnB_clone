#!/usr/bin/python3
from .base_model import BaseModel
"""
this class takes from the BaseModel class
"""


class Review(BaseModel):
    """
    public class attributes place_id, user_id,
    text
    """
    place_id = ""
    user_id = ""
    text = ""
