#!/usr/bin/python3
import json

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets a new object in __objects"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        serialized_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                serialized_objects = json.load(f)
                for key, value in serialized_objects.items():
                    class_name = key.split(".")[0]
                    obj = eval(class_name)(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
    def classes(self):
        """Returns classes"""
        classes = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review
        }
        return classes

    def attributes(self):
        """Returns classname and the attraibutes"""
        attributes = {
                "BaseModel":
                        {"id": str,
                        "created_at": datetime.datetime,
                        "updated_at": datetime.datetime},
                "User":
                         {"email": str,
                        "password": str,
                        "first_name": str,
                        "last_name": str},
                "State":
                        {"name": str},
                "City":
                        {"state_id": str,
                        "name": str},
                "Amenity":
                        {"name": str},
                "Place":
                        {"city_id": str,
                        "user_id": str,
                        "name": str,
                        "description": str,
                        "number_rooms": int,
                        "number_bathrooms": int,
                        "max_guest": int,
                        "price_by_night": int,
                        "latitude": float,
                        "longitude": float,
                        "amenity_ids": list},
                "Review":
                        {"place_id": str,
                        "user_id": str,
                        "text": str}
        }
        return attributes

