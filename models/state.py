#!/usr/bin/python3
""" Defines State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """ This is the State class that defines  the name attribute"""
    name = ""

    def __init(self, *arg, **kwarg):
        """initialises the state class"""
        super().__init__(self, *arg, **kwarg)
