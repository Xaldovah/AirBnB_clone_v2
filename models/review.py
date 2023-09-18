#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review classto store review information """
    place_id = ""
    user_id = ""
    text = ""

    def __str__(self):
        """Returns a string representation of the instance"""
        return "[Review] ({}) {}".format(self.id, self.__dict__)
