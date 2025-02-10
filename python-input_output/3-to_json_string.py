#!/usr/bin/python3
import json
"""This module provides the function to_json_string"""


def to_json_string(my_obj):
    """
    This function returns the representation in JSON
    of an object
    """
    return json.dumps(my_obj)
