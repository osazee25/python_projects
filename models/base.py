#!/usr/bin/python 3

class Base:
    """Base model which will serve as model for other classes
    Attributes:
        __nb_objects(int): the counter for number of objects"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialization for the Base class
        Args:
            id(int): Id of each of the objects that would be created"""
        self.id = id

        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

