#!/usr/bin/python3
"""Defines the User class"""
from models.base_model import BaseModel
class User(BaseModel):
    """This is the User class that defines different attributes of the user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    def __init__(self, *args, **kwargs):
        """This method initialises the class"""
        super().__init__(self,*args, **kwargs)
