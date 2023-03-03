#!/usr/bin/python3
"""
Contains the City class
"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """Representation of city"""
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    restaurants = relationship("Restaurant", backref="cities", cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """Initialises City"""
        super().__init__(*args, **kwargs)
