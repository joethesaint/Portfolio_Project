#!/usr/bin/python3
"""
Contains FoodReview Class
"""
import models
from models.base_model import Base, BaseModel
from models.user import User
from sqlalchemy import Column, String, Float, ForeignKey


class FoodReview(BaseModel, Base):
    """Representation of the FoodReview class"""
    __tablename__ = "foodreviews"
    food_id = Column(String(60), ForeignKey("foods.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    text = Column(String(1024), nullable=False)
    appearance = Column(Float, nullable=False)
    taste = Column(Float, nullable=False)
    quality = Column(Float, nullable=False)
    execution = Column(Float, nullable=False)
    rating = Column(Float, nullable=False)

    def __init__(self, *args, **kwargs):
        """Initialisation of FoodReview"""
        super().__init__(*args, **kwargs)
        self.rating = (self.appearance + self.taste + self.quality + self.execution) / 4


    
    def get_user(self):
        """Returns the user object that wrote the review"""
        return models.storage.get(User, self.user_id)
