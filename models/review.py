#!/usr/bin/python3
"""Defines the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ This is the Review class that defines place,
    user and review text if the review """
    place_id = ""
    user_id = ""
    text = ""
