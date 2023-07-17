#!/usr/bin/python3
"""
This is to be of a class User which will inherit from
class BaseModel in base_model.py
It will have public instances which are:
email, password, first_name, last_name.
and then we update the file_storage file to store
an also the console.py file to create and all methods involved.
"""
from .base_model import BaseModel


class User(BaseModel):
    """inherits from BaseModel- class BaseModel in base_model.py"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
