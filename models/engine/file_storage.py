#!/usr/bin/python3
# Todo

class FileStorage:
    def __init__(self, filepath, objects):
        self.__filepath = filepath
        self.__objects = objects
    def all(self):
        return self.__objects
    def new(self, obj):
        self.__objects = obj
    def save(self):

