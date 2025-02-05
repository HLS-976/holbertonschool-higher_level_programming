#!/usr/bin/python3
"""
This module provides the function is_same_class
"""


def is_same_class(obj, a_class):
    """
    This function returns True or False
    if a object is an instance of a class
    """
    return True if type(obj) == a_class else False
