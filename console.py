#!/usr/bin/python3
"""
This will be a program that is called console.py
it does contain the entry point for the command
interpreter.
then we have the module - cmd, and a class
class HBNBCommand(cmd.Cmd)
Then we have the commands - quit and EOF
help for the actions - it is there by default
a custom prompt - (hbnb)
and an empty line + ENTER should not do anything
The code cannot be imported
end the file with
if __name__ == '__main__':
    HBNBCommand().cmdloop()
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """the class and prompt as needed with cmd"""
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.strip()
        if class_name not in ['BaseModel']:
            print("** class doesn't exist **")
            return

        if class_name == 'BaseModel':
            new_instance = BaseModel()
        elif class_name == 'User':
            new_instance = User()

        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0].strip()
        if class_name not in ['BaseModel', 'User']:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1].strip()
        obj_key = "{}.{}".format(class_name, instance_id)
        objects = storage.all()
        if obj_key in objects:
            print(objects[obj_key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0].strip()
        if class_name not in ['BaseModel', 'User']:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1].strip()
        obj_key = "{}.{}".format(class_name, instance_id)
        objects = storage.all()
        if obj_key in objects:
            objects.pop(obj_key)
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print string representation of all instances"""
        args = arg.split()
        objects = storage.all()
        if not args:
            print([str(obj) for obj in objects.values()])
        elif args[0] in ['BaseModel', 'User']:
            print([str(obj) for obj in objects.values()])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance based on class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0].strip()
        if class_name not in ['BaseModel', 'User']:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1].strip()
        obj_key = "{}.{}".format(class_name, instance_id)
        objects = storage.all()
        if obj_key in objects:
            if len(args) < 3:
                print("** attribute name missing **")
                return

            attribute_name = args[2].strip()
            if len(args) < 4:
                print("** value missing **")
                return

            attribute_value = args[3].strip()
            instance = objects[obj_key]
            setattr(instance, attribute_name, attribute_value)
            instance.save()
        else:
            print("** no instance found **")

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF (Ctrl+D) is reached"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
