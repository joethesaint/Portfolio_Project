#!/usr/bin/python3

from models.base_model import Base, BaseModel


class FoodReview(BaseModel, Base):
    """Representation of the FoodReview class"""
    __tablename__ = "foodreviews"
    food_id = ""
    user_id = ""
    text = ""
    appearance = ""
    taste = ""
    quality = ""
    execution = ""

    def __init__(self, *args, **kwargs):
        """Initialisation of FoodReview"""
        super().__init__(*args, **kwargs)
