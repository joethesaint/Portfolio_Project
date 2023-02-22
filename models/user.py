#!/usr/bin/python3
"""
Contains the User Class
"""

from models.base_model import Base, BaseModel


class User(BaseModel, Base):
    """Representation of the User object"""
    first_name = ""
    last_name = ""
    email = ""
    password = ""

    def __init__(self, *args, **kwargs):
        """Initialisation of the User Class"""
        super().__init__(*args, **kwargs)
