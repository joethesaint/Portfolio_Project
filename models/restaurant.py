#!/usr/bin/python3
"""
Contains the Restaurant Class
"""

import models
from models.city import City
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

    def get_rating(self):
        """Gets the rating of a Restaurant and returns it as a dictionary"""
        rating_dict = {
            'ambience': 0,
            'cleanliness': 0,
            'service': 0,
            'uniqueness': 0,
            'total': 0
        }

        if len(self.reviews):
            for review in self.reviews:
                rating_dict['ambience'] += review.ambience
                rating_dict['cleanliness'] += review.cleanliness
                rating_dict['service'] += review.service
                rating_dict['uniqueness'] += review.uniqueness
                rating_dict['total'] += review.rating

            for key, rating in rating_dict.items():
                rating_dict[key] = rating / len(self.reviews)
        
        rating_dict['len'] = len(self.reviews)
        return rating_dict

        
    def price_range(self):
        """Get the min and max price in the restaurant menu"""
        price_dict = {
            'min': 0,
            'max': 0
        }
        price_list = []

        for food in self.foods:
            price_list.append(food.price)

        if price_list:
            price_dict['min'] = min(price_list)
            price_dict['max'] = max(price_list)

        return price_dict

    def get_city(self):
        """Get details if the city with the restaurant is locacted"""
        return models.storage.get(City, self.city_id)

