#!/usr/bin/python3
"""Contains the Review model"""
from tests.test_base_model import BaseModel

class Review(BaseModel):
    """Implements the Review model"""
    place_id = ""
    user_id = ""
    text = ""
