#!/usr/bin/python3
"""Database storage engine using SQLAlchemy for mysql+mysqldb connections."""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User

name2class = {
    'Amenity': Amenity,
    'City': City,
    'Place': Place,
    'State': State,
    'Review': Review,
    'User': User
}


class DBStorage:
    """Database Storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the database connection"""
        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, database),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Return all objects, or objects of a specific class"""
        self.reload()
        objects = {}
        if cls:
            if isinstance(cls, str) and cls in name2class:
                cls = name2class[cls]
            if isinstance(cls, type):
                for obj in self.__session.query(cls).all():
                    objects[obj.__class__.__name__ + '.' + obj.id] = obj
        else:
            for cls in name2class.values():
                for obj in self.__session.query(cls).all():
                    objects[obj.__class__.__name__ + '.' + obj.id] = obj
        return objects

    def reload(self):
        """Reload data from the database"""
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(session_factory)

    def new(self, obj):
        """Add a new object to the current session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the database"""
        if obj:
            self.__session.delete(obj)

    def close(self):
        """Close the current session"""
        self.__session.remove()

    def get(self, cls, id):
        """Retrieve an object based on class name and ID"""
        if isinstance(cls, str) and cls in name2class:
            cls = name2class[cls]
        return self.__session.query(cls).get(id)

    def count(self, cls=None):
        """Count the number of objects of a given class"""
        if cls and isinstance(cls, str) and cls in name2class:
            cls = name2class[cls]
            return self.__session.query(cls).count()
        elif not cls:
            total = 0
            for cls in name2class.values():
                total += self.__session.query(cls).count()
            return total
        return 0

