#!/usr/bin/python3
#TODO

from models.base_model import BaseModel
from models.state import State
import models
class City(BaseModel):
    state_id = "" # State.id
    name = ""

    def __init__(self, *arg, **kwarg):
        super().__init__(self, *arg, **kwarg)
