#!/usr/bin/python3
"""City Module that inherits from BaseModel and Base for HBNB project"""
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class City(BaseModel, Base):
    """a class that represents a city name
    Attributes:
        state_id: string - The state id
        name: string - The city name
        places: relationship - place, cascade, and backref
    """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")
