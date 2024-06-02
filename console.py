#!/usr/bin/python3
"""Console Module"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from ast import arg
from models import storage
valid_classes = {"BaseModel": BaseModel, "User": User, "Place": Place,
                 "State": State, "City": City, "Amenity": Amenity,
                 "Review": Review}

class HBNBCommand(cmd.Cmd):
    """Console Class"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Handles quit Command"""
        return True

    def do_EOF(self, line):
        """Handles eof Command"""
        return True

    def emptyline(self):
        """Does nothing when Enter is pressed"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
