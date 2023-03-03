#!/usr/bin/python
"""
Contains the Food class
"""

from models.base_model import Base, BaseModel
from models.restaurant import Restaurant
import models
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

    def get_rating(self):
        """Gets the rating of a Restaurant and returns it as a dictionary"""
        rating_dict = {
            'appearance': 0,
            'execution': 0,
            'quality': 0,
            'taste': 0,
            'total': 0
        }
        for review in self.reviews:
            rating_dict['appearance'] += review.appearance
            rating_dict['execution'] += review.execution
            rating_dict['quality'] += review.quality
            rating_dict['taste'] += review.taste
            rating_dict['total'] += review.rating
        if len(self.reviews):
            for rating in rating_dict.values():
                rating = rating / len(self.reviews)
        
        rating_dict['len'] = len(self.reviews)
        return rating_dict

    
    def get_restaurant(self):
        return models.storage.get(Restaurant, self.restaurant_id)
