#!/usr/bin/python3

import uuid
from datetime import datetime
class BaseModel:
    def __init__(self, *args, **kwargs):
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

    def __str__(self):
        return "[" + self.__class__.__name__ +"] (" + str(self.id) + ") " + str(self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
    def to_dict(self):
        self.__dict__["__class__"] = str(self.__class__.__name__)
        self.__dict__['created_at'] = str(self.created_at)
        self.__dict__['updated_at'] = str(self.updated_at)
        return self.__dict__
