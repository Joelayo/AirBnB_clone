#!/usr/bin/python3
"""This module contains a intepreter for the airbnb project"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

from models import storage
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """a class called hbnbcommand that is a subclass of cmd class"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Handles End Of File character.
        """
        print()
        return True

    def do_quit(self, line):
        """Exits the program.
        """
        return True

    def emptyline(self):
        """This overwrites the emptyline function"""
        pass

    def do_create(self, class_name=""):
        """Create an instance of a base model"""
        models = ["BaseModel", "User", "Place", "User",
                  "State", "City", "Amenity", "Review"]
        if class_name == "":
            print("** class name is missing **")
        elif class_name not in models:
            print("**class doesn't exit **")
        elif class_name == "BaseModel":
            instance = BaseModel()
            storage.new(instance)
            storage.save()
            print(instance.id)
        elif class_name == "User":
            instance = User()
            storage.new(instance)
            storage.save()
            print(instance.id)
        elif class_name == "Place":
            instance = Place()
            storage.new(instance)
            storage.save()
            print(instance.id)
        elif class_name == "State":
            instance = State()
            storage.new(instance)
            storage.save()
            print(instance.id)
        elif class_name == "City":
            instance = City()
            storage.new(instance)
            storage.save()
            print(instance.id)
        elif class_name == "Amenity":
            instance = Amenity()
            storage.new(instance)
            storage.save()
            print(instance.id)
        elif class_name == "Review":
            instance = Review()
            storage.new(instance)
            storage.save()
            print(instance.id)
        else:
            print("unknown operation")

    def do_show(self, line=""):
        """show the instance of the base model"""
        models = ["BaseModel", "User", "Place", "User", "State",
                  "City", "Amenity", "Review"]
        if line == "":
            print("** class name missing **")
        else:
            str = line.split()
            if str[0] not in models:
                print("** class doesn't exist **")
            elif len(str) == 1:
                print("** instance id missing **")
            else:
                obj = storage.all()
                key = str[0]+"."+str[1]
                if key in obj.keys():
                    print(obj[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, line):
        """delete the instance of the base model"""
        models = ["BaseModel", "User", "Place", "User", "State",
                  "City", "Amenity", "Review"]
        if line == "":
            print("** class name missing **")
        else:
            str = line.split()
            if str[0] not in models:
                print("** class doesn't exist **")
            elif len(str) == 1:
                print("** instance id missing **")
            else:
                obj = storage.all()
                key = str[0]+"."+str[1]
                if key in obj.keys():
                    del obj[key]
                else:
                    print("** no instance found **")

    def do_all(self, line=""):
        """show all the instances of the base model"""
        models = ["BaseModel", "User", "Place", "User", "State",
                  "City", "Amenity", "Review"]
        list = []
        obj = storage.all()
        if line == "":
            for key in obj.keys():
                list.append(obj[key])
            print(list)
        else:
            str = line.split()
            if str[0] not in models:
                print("** class doesn't exist **")
            elif len(str) > 1:
                print("** unknown operation **")
            else:
                for key in obj.keys():
                    class_name = key.split(".")
                    if class_name == str[0]:
                        list.append(obj[key])
                print(list)

    def do_update(self, line):
        """update the instance of the base model"""
        models = ["BaseModel", "User", "Place", "User", "State",
                  "City", "Amenity", "Review"]
        if line == "":
            print("** class name missing **")
        else:
            str = line.split()
            if str[0] not in models:
                print("** class doesn't exist **")
            elif len(str) == 1:
                print("** instance id missing **")
            else:
                obj = storage.all()
                key = str[0]+"."+str[1]
                if key in obj.keys():
                    if len(str) == 2:
                        print("** attribute name missing **")
                    elif len(str) == 3:
                        print("** value missing **")
                    else:
                        instance = obj[key]
                        attribute = str[2]
                        instance[attribute] = str[3]
                        print(instance)
                else:
                    print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
