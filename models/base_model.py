#!/usr/bin/python3
""" Defines the BaseModel class"""
import uuid
from datetime import datetime
import models

class BaseModel:
    """ This is BaseModel class that wii be inherited by other sub classes"""
    def __init__(self, *args, **kwargs):
        """ initialises the class """
        if kwargs and len(kwargs) != 0:
	    #self.__dict__.update(kwargs)
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "created_at":
                    fmt = "%Y-%m-%d %H:%M:%S.%f"
                    self.created_at = datetime.strptime(v, fmt)
                elif k == "updated_at":
                    fmt = "%Y-%m-%d %H:%M:%S.%f"
                    self.updated_at = datetime.strptime(v, fmt)
                elif k == "my_number":
                    self.my_number = v
                elif k == "name":
                    self.name = v
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ returns string representation of class name 
        and dictionary of attributes"""
        dic = self.__dict__
        if "__class__" in dic:
            dic.pop("__class__")
        return "[" + self.__class__.__name__ +"] (" + str(self.id) + ") " + str(dic)

    def save(self):
        """ calls save method from FileStorage class and updates time"""
        models.storage.save()
        self.updated_at = datetime.now()
    def to_dict(self):
        """ returns a dictionary of attributes of this instance"""
        self.__dict__["__class__"] = str(self.__class__.__name__)
        #self.__dict__['created_at'] = str(self.created_at)
        #self.__dict__['updated_at'] = str(self.updated_at)
        return self.__dict__
