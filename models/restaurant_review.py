#!/usr/bin/python3
"""
Contains RestaurantReview Class
"""
import models
from models.base_model import Base, BaseModel
from models.user import User
from sqlalchemy import Column, String, Float, Integer, ForeignKey


class RestaurantReview(BaseModel, Base):
    """Represents the RestaurantReview class"""
    __tablename__ = "restaurantreviews"
    restaurant_id = Column(String(60), ForeignKey('restaurants.id'), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    text = Column(String(1024), nullable="False")
    ambience = Column(Integer, nullable=False)
    service = Column(Integer, nullable=False)
    cleanliness = Column(Integer, nullable=False)
    uniqueness = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)


    def __init__(self, *args, **kwargs):
        """Initialisation of RestaurantReview"""
        super().__init__(*args, **kwargs)
        self.rating = (self.ambience + self.service + self.cleanliness + self.uniqueness) / 4


    def get_user(self):
        """Returns the user object that wrote the review"""
        return models.storage.get(User, self.user_id)

    # @property
    # def rating(self):
    #     return self.rating

    # @rating.setter
    # def rating(self):
    #     total_rate = 
    #     self.rating = total_rate / 4
