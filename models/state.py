#!/usr/bin/python3
""" State Module for HBNB project """
import uuid
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import models


class State(BaseModel, Base):
    """the state class"""
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship(
                'City', backref='state', cascade='all, delete-orphan')

    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initialize the class"""
        super().__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid4()

    @property
    def cities(self):
        """returns the list of City instances
        with state_id equals to the current State.id"""

        cities = []

        for k, v in models.storage.all(City).items():
            if v.state_id == self.id:
                cities.append(v)
        return cities

    def __repr__(self):
        """return a string representation of the object"""
        return "[State] ({}) {}".format(self.id, self.to_dict())
