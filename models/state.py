#!/usr/bin/python3
from models.base_model import BaseModel


class State(BaseModel):
    def __init__(self, *args, **kwargs):
        """Initialize State instance"""
        super().__init__(*args, **kwargs)
        self.name = ""

    def __str__(self):
        """Return a string representation of the State instance"""
        return "[State] ({}) {}".format(self.id, self.__dict__)
