#!/usr/bin/python3
"""Review module that inherits from BaseModel and Base for the HBNB project"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base


class Review(BaseModel, Base):
    """
    a class that represents a review
    Public class attributes:
        place_id: string - place id
        user_id: string - user id
        text: string - review description
    """
    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    text = Column(String(1024), nullable=False)
