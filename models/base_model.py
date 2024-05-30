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
                - __str__: prints a string representation of an instance.
            Public instance Methods:
                - save: updates the updated_at attribute with the current datetime. 
                - to_dict: returns a dictionary of instance attributes.

    """
    def __init__(self, id=None, created_at=None):
        """
            Private method initializes an object
            and generates a unique id using uuid4()
        """
        self.id = uuid.uuid4().hex
        self.created_at = datetime.now()