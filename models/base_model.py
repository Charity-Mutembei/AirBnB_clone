#!/usr/bin/python3
import uuid
from datetime import datetime
"""
These are modules that will aid generate the IDs for the created
instances of the class, - uuid
The date-time module will handle the date and time operation
"""
# Above you will find the imports
"""
This will be a base class named - BaseModel
it is to define the common attributes or methods
that other classes/subclasses will use.
Its public attributes are to be:
1. id, 2. created_at date, 3. updated_at
it should have __str__ instance, save, to_dict, etc.
"""


# defining the baseclass
class BaseModel:
    """
    step 1: initialize it
    Here we assign the ID every time the class is evoked - uuid.uuid4()
    We also convert the ID into string hence inside a str() method.
    we also intialize the created_at and updated_at attributes
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    # we have the save public method
    """
    The method save updates the update_at above
    with the current time the instance is run every time.
    """
    def save(self):
        self.updated_at = datetime.now()

    """
    we have the to_dict(self) method that will return a dictionary
    that does contain all values of the instance
    """
    def to_dict(self):
        """
        the method below __dict__ contains all objects and its values
        """
        obj_dict = self.__dict__.copy()
        """the method below has the class name of the object
        """
        obj_dict['__class__'] = self.__class__.__name__
        """the method below has the date the class was created
        """
        obj_dict['created_at'] = self.created_at.isoformat()
        """
        the method below contains when it was updated in the ISO format
        """
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    """
    The method below will return the objects representation as a string
    alternative of writing it -
    def __str__(self):
    return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    """
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
