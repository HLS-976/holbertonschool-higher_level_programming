#!/usr/bin/python3
"""
This module provides the function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    This function returns true or false if the object given
    is an instance of, or if the object is an instance of
    a class that inherited from, the specified class
    """
    return isinstance(obj, a_class)
