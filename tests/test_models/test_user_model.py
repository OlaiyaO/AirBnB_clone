#!/usr/bin/python3

'''
    All the test for the user model are implemented here.
'''

import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    '''
        Testing User class
    '''

    def setUp(self):
        '''
            Set up a new User instance before each test.
        '''
        self.new_user = User()

    def tearDown(self):
        '''
            Remove the User instance after each test.
        '''
        del self.new_user

    def test_user_inheritance(self):
        '''
            Test that the User class inherits from BaseModel.
        '''
        self.assertIsInstance(self.new_user, BaseModel)

    def test_user_attributes_existence(self):
        '''
            Test that user attributes exist.
        '''
        attributes = ['email', 'first_name', 'last_name', 'password']
        for attribute in attributes:
            with self.subTest(attribute=attribute):
                self.assertTrue(hasattr(self.new_user, attribute))

    def test_attribute_types(self):
        '''
            Test the types of user attributes.
        '''
        attribute_types = {'email': str, 'first_name': str, 'last_name': str, 'password': str}
        for attribute, data_type in attribute_types.items():
            with self.subTest(attribute=attribute):
                value = getattr(self.new_user, attribute)
                self.assertIsInstance(value, data_type)


if __name__ == '__main__':
    unittest.main()
