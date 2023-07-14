#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    def __init__(self, *args, **kwargs):
        """Initialize User instance"""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

    def __str__(self):
        """Return a string representation of the User instance"""
        return "[User] ({}) {}".format(self.id, self.__dict__)
