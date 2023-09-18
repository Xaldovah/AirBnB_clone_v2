#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import uuid

class Amenity(BaseModel):
    id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize State instance """
        super().__init__(*args, **kwargs)

        if "id" not in kwargs:
            self.id = str(uuid.uuid4())

    def __str__(self):
        """Returns a string representation of the instance"""
        return "[Amenity] ({}) {}".format(self.id, self.__dict__)
