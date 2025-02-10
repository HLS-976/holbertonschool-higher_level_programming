#!/usr/bin/python3
"""
This module provides the function from_json_string
"""
import json


def from_json_string(my_str):
    """
    This function return a python object by string json
    """
    return json.loads(my_str)
