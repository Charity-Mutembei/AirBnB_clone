#!/usr/bin/python3
# from base_model import BaseModel
from .base_model import BaseModel
"""
This is to be of a class User which will inherit from
class BaseModel in base_model.py
It will have public instances which are:
email, password, first_name, last_name.
and then we update the file_storage file to store
an also the console.py file to create and all methods involved.
"""


class User(BaseModel):
    """inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

