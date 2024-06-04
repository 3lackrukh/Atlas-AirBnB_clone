#!/usr/bin/python3
import models
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
                - save: updates the updated_at attribute with the
                current datetime.
                - to_dict: returns a dictionary of instance attributes.

    """
    def __init__(self, *args, **kwargs):
        """
            Private method initializes an object
            and generates a unique id using uuid4()
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            # Load from dictionary representation
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    v = datetime.strptime(v, time_format)
                if k != '__class__':
                    setattr(self, k, v)
                if "id" not in kwargs:
                    self.id = str(uuid.uuid4())
                    self.created_at = datetime.now()
                    self.updated_at = datetime.now()
        else:
            # New instance
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # Add new instance to storage
            models.storage.new(self)

    def __str__(self):
        """
            Returns a string representation of the instance
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__)

    def save(self):
        """
            Updates updated_at attribute with current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
            Returns a dictionary of instance attributes
        """
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        if isinstance(dic["created_at"], datetime):
            dic["created_at"] = self.created_at.isoformat()
        else:
            dic["created_at"] = self.created_at
        if isinstance(dic["updated_at"], datetime):
            dic["updated_at"] = self.updated_at.isoformat()
        else:
            dic["updated_at"] = self.updated_at
        return dic
