#!/usr/bin/python3
"""
Contains the BaseModel class
"""

from datetime import datetime
import models
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid

time = "%Y-%m-%dT%H:%M%S.%f"

Base = declarative_base()

class BaseModel:
    """The Model class from which future classes will be derived"""
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initialisation of the base models"""
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()

            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()

            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
    

    def __str__(self) -> str:
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)


    def to_dict(self):
        """Converts objects to its dictionary representation"""
        new_dict = self.__dict__.copy()

        if '_sa_instance_state' in new_dict:
            del new_dict['_sa_instance_state']

        if self.__class__.__name__ == 'Restaurant':
            new_dict['min'] = self.price_range()['min']
            new_dict['max'] = self.price_range()['max']
            new_dict['city'] = self.get_city().name

        if self.__class__.__name__ == 'Food':
            new_dict['restaurant_name'] = self.get_restaurant().name
            new_dict['restaurant_id'] = self.get_restaurant().id

        new_dict['no_of_reviews'] = self.get_rating()['len']
        new_dict['total_rate'] = self.get_rating()['total']
        return new_dict

    def save(self):
        """Updates the attribute 'updated_at' with the current datetime and saves the model to storage"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()


    def delete(self):
        """Deletes the current instance from the storage"""
        models.storage.delete(self)
