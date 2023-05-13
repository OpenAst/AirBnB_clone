#!/usr/bin/python3
"""The module that defines a user class"""

from models.base_model.py import BaseModel

class User(BaseModel):
    """the User class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
