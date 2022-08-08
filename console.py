#!/usr/bin/env python3
"""This module contains a intepreter for the airbnb project"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """a class called hbnbcommand that is a subclass of cmd class"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Implement the end-of-file prompt"""
        exit()

    def do_quit(self, line):
        """quit the command interpreter"""
        exit()

    def emptyline(self):
        """This overwrites the emptyline function"""
        pass

    def do_create(self, class_name=""):
        """Create an instance of a base model"""
        if class_name == "BaseModel":
            instance = BaseModel()
            storage.new(instance)
            storage.save()
            print(instance.id)
        elif class_name == "":
            print("** class name is missing **")
            pass
        elif class_name != "BaseModel":
            print("**class doesn't exit **")
        else:
            print("unknown operation")

    def do_show(self, class_name="", id=0):
        """show the instance of the base model"""
        if class_name == "":
            print("** class name missing **")
        pass

    def do_destroy(self):
        """delete the instance of the base model"""
        pass

    def do_all(self):
        """show all the instances of the base model"""
        pass

    def do_update(self):
        """update the instance of the base model"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
