#!/usr/bin/python3
import uuid
from datetime import datetime
"""
    This module defines the class BaseModel
    from which other classes will inherit.
"""


class BaseModel:
    """
        Attributes:
            - id(str): assigned using uuid at intialization.
            - created_at:
            - updated_at:
        Methods:
            Private instance Methods:
                - __str__: returns a string representation of an instance.
            Public instance Methods:
                - save: updates the updated_at attribute with the current datetime. 
                - to_dict: returns a dictionary of instance attributes.

    """
    def __init__(self, *args, **kwargs):
        """
            Private method initializes an object
            and generates a unique id using uuid4()
        """
        self.id = uuid.uuid4().hex
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
            Returns a string representation of the instance
        """
        return"[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__)

    def save(self):
        """
            Updates updated_at attribute with current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
            Returns a dictionary of instance attributes
        """
        dictionary = self.__dict__.copy()
        dictionary["created_at"] = dictionary["created_at"].isoformat()
        dictionary["updated_at"] = dictionary["updated_at"].isoformat()
        dictionary["__class__"] = self.__class__.__name__
        return dictionary
