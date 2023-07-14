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


class HBNBCommand(cmd.Cmd):
    """the class and prompt as needed with cmd"""
    prompt = '(hbnb) '

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
