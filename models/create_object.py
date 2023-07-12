#!/usr/bin/python3
"""
This is a class dedicate to the creation of objects and will be 
imported in the command interpreter class in the concole.py 
file for the complete functionality.
"""
class CreateObject:
    """
    this class is solely made for the
    functionality of the new object creation
    """
    def __init__(self, name):
        """intitialize the class""" 
        self.name = name

    def display(self):
        """see what we created here"""
        print(f"{self.name}")
