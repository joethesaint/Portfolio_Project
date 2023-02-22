#!/usr/bin/python
"""
Contains the Food class
"""

from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship


class Food(BaseModel, Base):
    """Represents Food """
    __tablename__ = "foods"
    name = Column(String(60), nullable=False)
    #cuisine_id = ""
    description = Column(String(1024), nullable=False)
    food_pic_name = Column(String(60), nullable=True)
    price = Column(Float, nullable=False)
    restaurant_id = Column(String(60), ForeignKey("restaurants.id"), nullable=False)
    reviews = relationship("FoodReview", backref="foods", cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """Initialisation of Food"""
        super().__init__(*args, **kwargs)
