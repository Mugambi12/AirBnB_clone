import cmd
import re
from shlex import split

import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()  # Print a new line before exiting
        return True

    def emptyline(self):
        """Handle empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of a model"""
        if not arg:
            print("** class name missing **")
        elif arg not in globals():
            print("** class doesn't exist **")
        else:
            instance = globals()[arg]()
            instance.save()
            print(instance.id)
            self.storage.save()

    def do_show(self, arg):
        """Show details of a model instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete a model instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                storage.all().pop(key)
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Show all instances of a model"""
        args = arg.split()
        if not arg:
            objects = storage.all().values()
        elif args[0] not in globals():
            print("** class doesn't exist **")
            return
        else:
            objects = [v for k, v in storage.all().items() if k.split(".")[0] == args[0]]
        print([str(obj) for obj in objects])

    def do_update(self, arg):
        """Update attributes of a model instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                instance = storage.all()[key]
                setattr(instance, args[2], args[3])
                instance.save()
            else:
                print("** no instance found **")

    def do_count(self, arg):
        """Count the number of instances of a model"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        else:
            count = len([v for k, v in storage.all().items() if k.split(".")[0] == args[0]])
            print(count)

    def do_exit(self, arg):
        """Exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
