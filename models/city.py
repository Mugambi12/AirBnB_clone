#!/usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    def __init__(self, *args, **kwargs):
        """Initialize City instance"""
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""

    def __str__(self):
        """Return a string representation of the City instance"""
        return "[City] ({}) {}".format(self.id, self.__dict__)
