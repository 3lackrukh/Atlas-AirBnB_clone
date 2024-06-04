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
            print("** class name missing **") # prints error if no class name is given
            return False # returns false indicating error

        parsed_val = value.split(' ') # splits input string into separate words
        if parsed_val[0] not in valid_classes.keys():
            print("** class doesn't exist **") 
            return False

        return True # returns true if class name is valid

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

        return key # returns if key instance is valid

    def do_create(self, arg):
        """Creates a new instance of an object"""
        if self.check_class(arg):
            new = valid_classes[arg]()  #creates new instance of specified class
            new.save()  #saves new instance
            print(new.id)  #prints id of new instance

    def do_show(self, arg):
        """Prints string based on class and id"""
        if self.check_class(arg):
            word = arg.split(' ')  #splits string into separate words
            if self.valid_instance(word):
                key = "{}.{}".format(word[0], word[1])  #createsa key to look up instance
                print(storage.all()[key])  #prints the instance

    def do_all(self, arg):
        """Prints all instances"""
        if arg != "":
            word = arg.split(' ')
            if word[0] not in valid_classes.keys():
                print("** class doesn't exist **")
            else:
                n = [
                    str(obj) for key, obj in storage.all().items()
                    if type(obj).__name__ == word[0]  # only include instances of the specified class
                ]
                print(n) # prints all instances of that class
        else:
            n = [str(obj) for key, obj in storage.all().items()] #include all instances
            print(n)  #prints all instances

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id"""
        if self.check_class(arg):
            word = arg.split(' ')
            valid_key = self.valid_instance(word)
            if valid_key:
                del storage.all()[valid_key]  # deletes the instance
                storage.save()  #saves the changes

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
                    print("** attribute name missing **") #Prints if no name is provided
                    return False
                if len(word) < 4:
                    print("** value missing **")
                    return False
                if valid_key in storage.all().keys():
                    setattr(storage.all()[valid_key], word[2],
                            word[3].strip('\'"'))  #update the attribute


if __name__ == "__main__":
    HBNBCommand().cmdloop()  #starts the command loop
