#!/usr/bin/python3
"""Module for State class"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """Class representing a State"""
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initialize state"""
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Getter attribute for cities, returns list of City instances"""
            city_instances = models.storage.all("City").values()
            city_list = [city for city in city_instances if city.state_id == self.id]
            return city_list
