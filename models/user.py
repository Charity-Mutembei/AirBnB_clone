#!/usr/bin/python3
"""Defines the class User which."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a User class model.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
