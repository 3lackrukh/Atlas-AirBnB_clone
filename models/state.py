#!/usr/bin/python3
"""State Subclass"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class"""
    def __init__(self):
        self.name = ""
