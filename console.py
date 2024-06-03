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

    def valid_instance(self, value):
        """ Check if:
        a) instance name is given
        b) instance name exists in valid_instances dictionary
        """
        if len(value) < 2:
            print("** instance id missing **")
            return False

        key = "{}.{}".format(value[0], value[1])
        if key not in storage.all().keys():
            print("** no instance found **")
            return False

        return key

    def do_create(self, arg):
        """Creates a new instance of an object"""
        if self.check_class(arg):
            new = valid_classes[arg]()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """Prints string based on class and id"""
        if self.check_class(arg):
            word = arg.split(' ')
            if self.valid_instance(word):
                key = "{}.{}".format(word[0], word[1])
                print(storage.all()[key])

    def do_all(self, arg):
        """Prints all instances"""
        if arg != "":
            word = arg.split(' ')
            if word[0] not in valid_classes.keys():
                print("** Class does not exist **")
            else:
                n = [
                    str(obj) for key, obj in storage.all().items()
                    if type(obj).__name__ == word[0]
                ]
                print(n)
        else:
            n = [str(obj) for key, obj in storage.all().items()]
            print(n)


    def do_update(self, arg):
        """
        Updates based on class and ID with
        add/update attributes
        """
        if self.check_class(arg):
            word = arg.split(' ')
            valid_key = self.valid_instance(word)
            if valid_key:
                if len(word) < 3:
                    print ("** Attribute name is missing **")
                    return False
                if len(word) > 4:
                    print ("** Value is missing **")
                    return False
                if valid_key in storage.all().keys():
                    setattr(storage.all()[valid_key], word[2], word[3].strip('\'"'))

if __name__ == "__main__":
    HBNBCommand().cmdloop()
