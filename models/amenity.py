#!/usr/bin/python3
"""Amenity class Module that inherits from BaseModel and Base
for HBNB project"""
from models.base_model import BaseModel, Base
from models.place import place_amenity
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """
    a class that represents an amenity
    Public class attributes:
        name: string - amenity name
        place_amenities: relationship - place and secondary(place_amenity)
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
