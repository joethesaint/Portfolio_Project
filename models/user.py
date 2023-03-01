#!/usr/bin/python3
"""
Contains the User Class
"""

from hashlib import md5
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Representation of the User object"""
    __tablename__ = "users"
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    email = Column(String(128), nullable=False)#, unique=True
    password = Column(String(128), nullable=False)
    restaurant_reviews = relationship("RestaurantReview", backref="users", cascade="all, delete, delete-orphan")
    food_reviews = relationship("FoodReview", backref="users", cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """Initialisation of the User Class"""
        super().__init__(*args, **kwargs)
        self.password = md5(bytes(self.password, 'UTF-8')).hexdigest()
