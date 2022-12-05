#!/usr/bin/python3
""" Defines the city class"""

from models.base_model import BaseModel
from models.state import State
import models


class City(BaseModel):
    """ This is the city class that defines
    different attributes of the class """
    state_id = ""  # State.id
    name = ""

    def __init__(self, *arg, **kwarg):
        """This method initialises the class"""
        super().__init__(self, *arg, **kwarg)
