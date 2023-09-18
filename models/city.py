#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""

    def __str__(self):
        """Returns a string representation of the instance"""
        return "[City] ({}) {}".format(self.id, self.__dict__)
