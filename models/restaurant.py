#!/usr/bin/python3
"""
Contains the Restaurant Class
"""

from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Restaurant(BaseModel, Base):
    """Representation of Restaurant"""
    __tablename__ = 'restaurants'
    name = Column(String(120), nullable=False)
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    description = Column(String(1024), nullable=False)
    display_pic_name = Column(String(60), nullable=True)
    address = Column(String(120), nullable=False)
    foods = relationship("Food", backref="restaurants", cascade="all, delete, delete-orphan")
    reviews = relationship("RestaurantReview", backref="restaurants", cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """Initialises Restaurant"""
        super().__init__(*args, **kwargs)
