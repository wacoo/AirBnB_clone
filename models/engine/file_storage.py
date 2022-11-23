#!/usr/bin/python3
# Todo
import json
import sys

sys.path.append('../models')
from models.base_model import BaseModel
import os.path

class FileStorage:
    def __init__(self):
        self.__filepath = "file.json"
        self.__objects = {}
    def all(self):
        return self.__objects
    def new(self, obj):
        self.__objects[obj.__class__.__name__+"."+ obj.id] = obj
        
    def save(self):
        list_of_dicts = []
        with open("file.json", 'w') as jfile:
            if self.__objects is None:
                jfile.write("[]")
            else:
                for k, v in self.__objects.items():
                    jfile.write(json.dumps(v.to_dict()))
                    jfile.write("\n")

    def reload(self):
        file_exists = os.path.exists('file.json')
        if file_exists:
            obj_list = []
            with open("file.json", 'r') as jfile:
                for obj in jfile:
                    obj_dict = json.loads(obj)
                    #obj_list.append(obj_dict)
                    objc = BaseModel(obj_dict)
                    self.__objects[objc.__class__.__name__ + "." + objc.id] = objc
                    #for x in obj_list:
                        #objc = BaseModel(x)
                        #self.__objects[objc.__class__.__name__ + "." + objc.id] = objc

