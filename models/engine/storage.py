#!/usr/bin/python3
"""
Contains the DBStorage Class
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import models
from models.base_model import Base
from models.city import City
from models.restaurant import Restaurant
from models.food import Food
from models.user import User
from models.food_review import FoodReview
from models.restaurant_review import RestaurantReview

classes = {"food": Food, "city": City, "Restaurant": Restaurant, "User": User, "FoodReview": FoodReview, "RestaurantReview": RestaurantReview}

class DBStorage():
    """Representation of DBStorage class"""
    __engine = None
    __session = None
    
    def __init__(self) -> None:
        MYSQL_USER = "foodfind_dev"
        MYSQL_PWD = "foodfind_dev_pwd"
        MYSQL_HOST = "localhost"
        MYSQL_DB = "foodfind_db"
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(MYSQL_USER, MYSQL_PWD, MYSQL_HOST, MYSQL_DB))


    def all(self, cls=None):
        """query on the current database session"""
        obj_list = []
        for clss in classes:
            if cls is None or cls is classes[clss] or cls == clss:
                objs = self.__session.query(classes[clss]).all()
                obj_list.extend(objs)
        return obj_list

    def reload(self):
        """reloads data from database"""
        Base.metadata.create_all(self.__engine)
        session_maker = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_maker)
        self.__session = Session

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def close(self):
        """call remove method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """Returns the object based on the class name and its Id, or None if not found"""
        if cls not in classes.values():
            return None

        all_objs = models.storage.all(cls)
        for obj in all_objs:
            if obj.id == id:
                return obj

        return None
        
