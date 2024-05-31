#!/usr/bin/python3
"""Console Module"""
import cmd
from models.base_model import BaseModel

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