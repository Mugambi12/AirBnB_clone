#!/usr/bin/python3
import json

from tests.test_base_model import BaseModel
from tests.test_user import User
from tests.test_state import State
from tests.test_amenity import Amenity
from tests.test_city import City
from tests.test_place import Place
from tests.test_review import Review


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
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                serialized_objects = json.load(file)
                for key, value in serialized_objects.items():
                    class_name = key.split(".")[0]
                    obj = eval(class_name)(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
