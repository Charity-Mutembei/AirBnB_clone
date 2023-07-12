#!/usr/bin/python3
import cmd, sys
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
        self.objects = {}

    def run(self):
        while True:
            command = input("Enter your command here: ")
            self.process_command_command(command)
            """the command  process_command is made below"""

    def process_command(self, command):
        """This will split the command into tokens"""
        tokens = command.split()
        if len(tokens) == 0:
            return
        else:
            """take the commands and extract the command and its arguments"""
            cmd = tokens[0]
            args = tokens[1:]
            """now we can call the methods that become cmd"""
        if cmd == "create":
            self.create_object(args)
        elif cmd == "retrieve":
            self.retrieve_object(args)
        elif cmd == "operations":
            self.perform_operations(args)
        elif cmd == "update":
            self.update_object(args)
        elif cmd == "destroy":
            self.destroy_object(args)
        else:
            print ("Type - help - for the commands available")

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    CommandInterpreter( ) .cmdloop()