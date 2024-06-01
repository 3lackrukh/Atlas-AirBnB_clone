#!/usr/bin/python3
"""User Subclass"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class"""
    user_email = ""
    user_password = ""
    user_first_name = ""
    user_last_name = ""