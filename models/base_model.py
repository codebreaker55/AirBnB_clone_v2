#!/usr/bin/python3
"""This module defines a base class for all models in the hbnb project"""
import models
import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """
    Representing the BaseModel class:
        that defines all common attributes/methods for other classes
    """
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))

    def __init__(self, *args, **kwargs):
        """
        Instantiation of the base model class
        Public instance attributes:
            id: string - assign with an uuid when an instance is created
            created_at: datetime - assign with the current datetime,
            when an instance is created.
            updated_at: datetime - assign with the current datetime,
            when an instance is created.
            and it will be updated every time the object is changed.
        Args:
            *args (any): not used
            **kwargs: Key and value arguments for the constructor,
            of the BaseModel
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
        a function that returns a string
        Return:
            a string of class name, id, and dictionary
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """a function that returns  a string representaion"""
        return self.__str__()

    def save(self):
        """
        a function that updates the public instance attribut,
        eupdated_at to current
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        a function that creates a dictionary of the class and then returns
        Return:
            returns a dictionary of all the key values in (__dict__)
        """
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        if '_sa_instance_state' in my_dict.keys():
            del my_dict['_sa_instance_state']
        return my_dict

    def delete(self):
        """ a funcction that deletes the object"""
        models.storage.delete(self)
