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
    created_objects = []
    """we created a storage ideas above with the dictionary"""

    def __init__(self, name):
        """intitialize the class""" 
        self.name = name
        """add the objects created"""
        self.created_objects.append(self)

    def display(self):
        """see what we created here"""
        print(f"{self.name}")
