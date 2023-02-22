#!/usr/bin/python
"""
Contains the Food class
"""

from models.base_model import Base, BaseModel


class Food(BaseModel, Base):
    """Represents Food """
    __tablename__ = "foods"
    name = ""
    cuisine_id = ""
    description = ""
    pic = ""
    price = ""

    def __init__(self, *args, **kwargs):
        """Initialisation of Food"""
        super().__init__(*args, **kwargs)
