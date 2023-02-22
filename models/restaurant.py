#!/usr/bin/python3
"""
Contains the Restaurant Class
"""

from models.base_model import Base, BaseModel
from sqlalchemy import Column


class Restaurant(BaseModel, Base):
    """Representation of Restaurant"""
    __tablename__ = 'restaurants'
    name = ""
    city_id = ""
    description = ""
    pic = ""
    address = ""

    def __init__(self, *args, **kwargs):
        """Initialises Restaurant"""
        super().__init__(*args, **kwargs)
