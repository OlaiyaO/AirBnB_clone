#!/usr/bin/python3

"""Test - the console"""

import unittest
import console
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    """class test console"""

    def setUp(self):
        """set up the instance"""
        self.console_instance = HBNBCommand()

    def test_quit(self):
        """test for the method quit"""
        result = self.console_instance.onecmd("quit")
        self.assertTrue(result)

    def test_EOF(self):
        """test for the method EOF"""
        result = self.console_instance.onecmd("EOF")
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
