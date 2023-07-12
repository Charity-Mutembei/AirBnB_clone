#!/usr/bin/python3
import cmd, sys
from create_object import CreateObject
"""
This is a file that contains the command interpreter code
and this is to be run to excute the command interpreter.
It will contain classes and substancess/instances for the methods. 
"""

class CommandInterpreter(cmd.Cmd):
    """the basic structure of the command interpreter which is to handle the input of the user"""
    def __init__(self):
        """
        the constructor for the class 
        the intialization about below creates a dictionary for the sotarge of obejcts
        """
        super().__init__()
    
    def do_create_object(self, name):
        """we have imported the CreateObject class for this functionality"""
        obj = CreateObject(name)
        print(f"{obj.name} created")
        self.verify_object_creation(obj)

    def verify_object_creation(self, obj):
        """this is just a precaution to confirm that the object was created"""
        if obj.name:
            print("the object is verfied")
        else:
            print("object creation failed")

    def do_EOF(self, line):
        return True
if __name__ == '__main__':
    CommandInterpreter( ) .cmdloop()