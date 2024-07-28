#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City",
                              back_populates="state",
                              cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            """Getter method for cities linked to this state"""
            return [
                    city for city in models.storage.all(City).values()
                    if city.state_id == self.id
            ]
