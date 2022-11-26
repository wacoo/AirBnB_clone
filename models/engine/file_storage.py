#!/usr/bin/python3
# Todo
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
    #Class Names
    #clss = {"BaseModel", "User", "State", "City", "Amenity", "Place", "Review"}
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
                    jfile.write(json.dumps(v.to_dict(), default=str))
                    jfile.write("\n")

    def reload(self):
        file_exists = os.path.exists('file.json')
        if file_exists:
            obj_list = []
            with open("file.json", 'r') as jfile:
                objc = None
                for obj in jfile:
                    obj_dict = json.loads(obj)
                    #obj_list.append(obj_dict)
                    for key in obj_dict.keys():
                        if obj_dict["__class__"] == "BaseModel":
                            objc = BaseModel(obj_dict)
                            break
                        elif obj_dict["__class__"] == "User":
                            objc = User(obj_dict)
                            break
                        elif obj_dict["__class__"] == "State":
                            objc = State(obj_dict)
                            break
                        elif obj_dict["__class__"] == "City":
                            objc = City(obj_dict)
                            break
                        elif obj_dict["__class__"] == "Amenity":
                            objc = Amenity(obj_dict)
                            break
                        elif obj_dict["__class__"] == "Place":
                            objc = Place(obj_dict)
                            break
                        elif obj_dict["__class__"] == "Review":
                            objc = Review(obj_dict)
                            break
                    self.__objects[objc.__class__.__name__ + "." + objc.id] = objc
                    #for x in obj_list:
                        #objc = BaseModel(x)
                        #self.__objects[objc.__class__.__name__ + "." + objc.id] = objc

