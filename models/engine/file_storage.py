#!/usr/bin/python3
# Todo
import json
import sys

sys.path.append('../models')
from models.base_model import to_dict
class FileStorage:
    def __init__(self, filepath, objects):
        self.__filepath = filepath
        self.__objects = objects
    def all(self):
        return self.__objects
    def new(self, obj):
        self.__objects[self.__class__.__name__.id] = obj
    def save(self):
        with open("file.json", "w") as jfile:
            if self.__objects is None:
                jfile.write("[]")
            else:
                list_of_dicts = [d.to_dict() for d in self.__objects]
                jfile.write(json.dumps(list_of_dicts))
