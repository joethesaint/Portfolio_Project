#!/usr/bin/python3
"""
Contains RestaurantReview Class
"""

from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, Float, ForeignKey


class RestaurantReview(BaseModel, Base):
    """Represents the RestaurantReview class"""
    __tablename__ = "restaurantreviews"
    restaurant_id = Column(String(60), ForeignKey('restaurants.id'), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    text = Column(String(1024), nullable="False")
    ambience = Column(Float, nullable=False)
    service = Column(Float, nullable=False)
    cleanliness = Column(Float, nullable=False)
    uniqueness = Column(Float, nullable=False)


    def __init__(self, *args, **kwargs):
        """Initialisation of RestaurantReview"""
        super().__init__(*args, **kwargs)
