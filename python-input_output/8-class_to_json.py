#!/usr/bin/python3
"""This module provides the function class_to_json"""


def class_to_json(obj):
    """
    This function returns the dictionnary description
    of an object
    """
    return obj.__dict__
