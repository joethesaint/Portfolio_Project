#!/usr/bin/python3
"""
Contains RestaurantReview Class
"""

from models.base_model import Base, BaseModel


class RestaurantReview(BaseModel, Base):
    """Represents the RestaurantReview class"""
    __tablename__ = "restaurantreviews"
    restaurant_id = ""
    user_id = ""
    text = ""
    ambience = ""
    service = ""
    cleanliness = ""
    uniqueness = ""


    def __init__(self, *args, **kwargs):
        """Initialisation of RestaurantReview"""
        super().__init__(*args, **kwargs)
