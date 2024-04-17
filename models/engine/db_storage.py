#!/usr/bin/python3
"""initializing the class DBStorage"""
import models
from models.base_model import BaseModel, Base
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """
    Private class attributes:
        __engine: set to None
        __session: set to None
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Public instance methods:
        __init__(self):
            create the engine (self.__engine)
            the engine must be linked to the MySQL database
            and user created before (hbnb_dev and hbnb_dev_db):
                dialect: mysql
                driver: mysqldb
            all of the following values must be retrieved via,
            environment variables:
                MySQL user: HBNB_MYSQL_USER
                MySQL password: HBNB_MYSQL_PWD
                MySQL host: HBNB_MYSQL_HOST (here = localhost)
                MySQL database: HBNB_MYSQL_DB
        """
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """a function that set query on the current database session"""

        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """a function that adds the object to the current database session"""

        self.__session.add(obj)

    def save(self):
        """
        a function that commits all changes,
        of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        a function that deletes from the current database session obj
        if not None
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """a function that reloads data from the database"""

        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """
        a function that calls remove() method
        on the private session attribute
        """
        self.__session.remove()
