#!/usr/bin/python3
"""models/city inherits from the class BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """city class which inherits from the Basemodel class """

    state_id = ""
    name = ""
