#!/usr/bin/python3
"""
This module provides the function inherits
"""


def inherits_from(obj, a_class):
    """
    This function returns true or false if an object
    is an instance of a class that inherited
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
