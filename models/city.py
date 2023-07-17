#!/usr/bin/python3
"""
This class takes from the BaseModel class
"""
from .base_model import BaseModel


class City(BaseModel):
    """
    Public attributes are state_id and name
    """
    state_id = ""
    name = ""
