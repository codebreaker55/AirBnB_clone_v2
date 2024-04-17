#!/usr/bin/python3
"""This module defines a class Use that inherits from BaseModel and Base"""
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
    """
    a class User that inherits from BaseModel and Base
    Public class attributes:
        email: string -  email address
        password: string - password for login
        first_name: string - first name
        last_name: string - last name
        places: relationship - Place, cascade(delete),  and backref(user)
        reviews: relationship - Review, cascade(delete), and backref(user)
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="user")
    reviews = relationship("Review", cascade='all, delete, delete-orphan',
                           backref="user")
