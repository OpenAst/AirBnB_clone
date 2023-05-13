#!/usr/bin/python3
"""A module that create a Review class"""

from models/base_model.py import BaseModel

class Review(BaseModel):
    """The Review class"""

    place_id = ""
    user_id = ""
    text = ""
