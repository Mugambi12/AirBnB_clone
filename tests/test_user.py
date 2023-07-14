#!/usr/bin/python3
from tests.test_base_model import BaseModel


class User(BaseModel):
    def __init__(self, *args, **kwargs):
        """Initialize User instance"""
        super().__init__(*args, **kwargs)
        self.email = "airbnb@mail.com"
        self.password = "root"
        self.first_name = "Betty"
        self.last_name = "Bar"

    def __str__(self):
        """Return a string representation of the User instance"""
        return "[User] ({}) {}".format(self.id, self.__dict__)
