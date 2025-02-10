#!/usr/bin/python3
"""This module provides the function to_json_string"""
import json

def to_json_string(my_obj):
    """
    This function returns the representation in JSON
    of an object
    """
    return json.dumps(my_obj)
