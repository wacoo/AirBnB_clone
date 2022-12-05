#!/usr/bin/python3
""" Defines the FileStorage class"""
import json
import sys

sys.path.append('../models')
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User
import os.path

class FileStorage:
    """This is the FileStorage class that creates, displays 
    and reloads saved objects form json file
    
    Attributes:
    __filepath (str): path to a file to be saved
    __objects (dic): a dictionary of create objects
    """
    __filepath = "file.json"
    __objects = {}
    """def __init__(self):
        Initialises the class
        self.__filepath = "file.json"
        self.__objects = {}"""
    def all(self):
        """Returns all the objects created"""
        return self.__objects
    def new(self, obj):
        """Adds a new object"""
        FileStorage.__objects[obj.__class__.__name__+"."+ obj.id] = obj
        
    def save(self):
        """Serialises __objects to JSON file located __filepath"""
        dic = FileStorage.__objects
        dic_obj = {obj: dic[obj].to_dict() for obj in dic.keys()}
        with open("file.json", 'w') as jfile:
            json.dump(dic_obj, jfile, default=str)

    def reload(self):
        """Deserialises the JSON data located at __filepath to __objects"""
        file_exists = os.path.exists('file.json')
        if file_exists:
            obj_list = []
            with open("file.json", 'r') as jfile:
                objc = None
                obj_dict = json.load(jfile)
                    #obj_list.append(obj_dict)
                for v in obj_dict.values():
                    c_name = v["__class__"]
                    del v["__class__"]
                    self.new(eval(c_name)(**v))

                    #for x in obj_list:
                        #objc = BaseModel(x)
                        #self.__objects[objc.__class__.__name__ + "." + objc.id] = objc

