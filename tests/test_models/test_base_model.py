#!/usr/bin/python3
"""
Function that defines unnitest tests
"""
import os
import unittest
import inspect
import pep8
from models.base_model import BaseModel
from datetime import datetime
from models.base_model import storage

class BaseModelTest(unittest.TestCase):
    """ Tests/checkes BaseModel"""
    def setUp(self):
        ''' function that creates instances. '''
        self.obj = BaseModel()
    
    def test_initialization_with_kwargs(self):
        """
        initialized with keyword arguments (kwargs).
        Creates a dictionary of keyword arguments.
        Uses various assert methods to check instance
        if has the correct values for its id, 
        'created_at', 'updated_at', and 'custom_attr' attributes.
        """
        kwargs = {
            'id': '123',
            'created_at': '2023-07-15T12:00:00',
            'updated_at': '2023-07-15T13:00:00',
            'custom_attr': 'value'
        }
        self.obj = BaseModel(**kwargs)
        self.assertEqual(self.obj.id, '123')
        self.assertEqual(self.obj.created_at, datetime(2023, 7, 15, 12, 0, 0))
        self.assertEqual(self.obj.updated_at, datetime(2023, 7, 15, 13, 0, 0))
        self.assertEqual(self.obj.custom_attr, 'value')
        storage.new.assert_called_once_with(self.obj)
        storage.save.assert_called_once()
    
    def test_init_without_kwargs(self):
    """ Testing the "BaseModel" class' constructor,
    The code ensures that the "id", "created_at", 
    and "updated_at" attributes are set correctly
    """
        self.assertIsNotNone(self.obj.id)
        self.assertIsNotNone(self.obj.created_at)
        self.assertIsNotNone(self.obj.updated_at)
        storage.new.assert_called_once_with(self.obj)
        storage.save.assert_called_once()
    
    def test_save(self):
        '''
        sets the updated_at attribute 
        of the self.obj object to None.
        '''
        self.obj.updated_at = None
        self.obj.save()
        '''
        checks if the updated_at attribute of the self.obj 
        object is not None. If it is None, the test will fail.
        '''
        self.assertIsNotNone(self.obj.updated_at)
        """
        Checks if the save() method of the storage object 
        has been called exactly once. 
        If it hasn't been called or has been called 
        multiple times, the test will fail.
        """
        storage.save.assert_called_once()
    
    def test_to_dict(self):
        '''
        sets the id attribute of 
        self.obj to the string '123'.
        '''
        self.obj.id = '123'
        '''
        sets the created_at attribute of 
        self.obj to a datetime object
        '''
        self.obj.created_at = datetime(2023, 7, 15, 12, 0, 0)
        '''
        sets the updated_at attribute of 
        self.obj to a datetime object 
        '''
        self.obj.updated_at = datetime(2023, 7, 15, 13, 0, 0)
        expected_dict = {
            'id': '123',
            '__class__': 'BaseModel',
            'created_at': '2023-07-15T12:00:00',
            'updated_at': '2023-07-15T13:00:00'
        }
        self.assertEqual(self.obj.to_dict(), expected_dict)
    
    def test_str(self):
        '''
        sets the id attribute of the self.obj object
        '''
        self.obj.id = '123'
        '''
        sets the __dict__ attribute of self.obj to a 
        dictionary with two key-value pairs, where 
        'key1' maps to 'value1' and 'key2' maps to 'value2'.
        '''
        self.obj.__dict__ = {'key1': 'value1', 'key2': 'value2'}
        '''
        defines the expected string representation of the object
        '''
        expected_str = '[BaseModel] (123) {"key1": "value1", "key2": "value2"}'
       '''
       asserts that calling str(self.obj) 
       should return the same string as expected_str
       '''
       self.assertEqual(str(self.obj), expected_str)

if __name__ == '__main__':
    unittest.main()
