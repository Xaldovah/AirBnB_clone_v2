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

    name = Column(String(128), nullable=Fasle)

    if getenv('HBNB_TYPE_STORAGE') = 'db':
        cities = relationship('City', backref='state', cascade='all, delete-orphan')

    else:
        name = ""

    @property
    def cities(self):
        """returns the list of City instances
        with state_id equals to the current State.id"""
       
        cities = []

        for k, v in models.storage.all(City).items():
            if v.state_id == self.id:
                cities.append(v)
        return cities

