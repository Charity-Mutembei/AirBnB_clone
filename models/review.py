#!/usr/bin/python3
"""
this class takes from the BaseModel class
"""
from .base_model import BaseModel


class Review(BaseModel):
    """
    public class attributes place_id, user_id,
    text
    """
    place_id = ""
    user_id = ""
    text = ""
