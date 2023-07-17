#!/usr/bin/python3
"""
This class inherits from the class BaseModel
"""
from .base_model import BaseModel


class State(BaseModel):
    """
    has the public attributes to be name which
    should be an empty string
    """
    name = ""
