#!/usr/bin/python3
"""
This module provides a function that prints string in output
It takes two strings in argument and print sentence with them
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name - Prints a sentence with first_name and last_name

    first_name -- A string
    las_name -- A string

    This function checks if the two arguments are string and prints
    a sentence else throws an error with the following message
    "first_name/last_name must be a string"
    """
    if not (isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if not (isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
