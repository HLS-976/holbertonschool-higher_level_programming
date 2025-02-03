#!/usr/bin/python3
"""
This module provides a the lookup function
that returns the list of attributes of an object
"""


def lookup(obj):
    """
    This function returns the number of available
    attribute and methods of an object
    """
    return(dir(obj))
