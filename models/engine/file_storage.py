#!/usr/bin/python3
import json
# from user import User
from ..user import User
from models.base_model import BaseModel
"""
This is a class FileStorage that serializes the instances in
BaseModel class and also deserializes the same JSON file
to instances
"""


class FileStorage:
    # private attributes
    """the file path to the .json file"""
    __file_path = "file.json"
    """the objects equal a dictionary"""
    __objects = {}

    # public instances
    def classes(self):
        """Returns a dictionary of supported classes for serialization"""
        return {
            "BaseModel": BaseModel,
            "User": User,
        }
    
    def all(self):
        """returns all the objects"""
        return self.__objects

    def new(self, obj):
        """sets in the objects the obj with key/id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """takes the objects and saves in Json format"""
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        try:
            with open(self.__file_path, 'w') as file:
                json.dump(obj_dict, file)
        except Exception as e:
            print("Error saving ojects to the file:", e)

    def reload(self):
        """deserializes the Json file if its found following the path"""
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    class_obj = globals()[class_name]
                    self.__objects[key] = class_obj(**value)
        except FileNotFoundError:
            pass
        except Exception as e:
            print("Error reloading objects from file:", e)
