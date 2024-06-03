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

    def check_class(self, value):
        """ Check if:
        a) a class name is given
        b) class name exists in valid_classes dictionary
        """
        if value == "" or value is None:
            print("** Class name missing **")
            return False

        parsed_val = value.split(' ')
        if parsed_val[0] not in valid_classes.keys():
            print("** Class does not exist **")
            return False

        return True

    def do_show(self,arg):
        """Prints string based on class and id"""
        if self.check_class(arg):
            word = arg.split(' ')
            if self.valid_instance(word):
                key = "{}.{}".format(word[0], word[1])
                print(storage.all()[key])

    def do_create

    def do_update

    def do_all


if __name__ == "__main__":
    HBNBCommand().cmdloop()
