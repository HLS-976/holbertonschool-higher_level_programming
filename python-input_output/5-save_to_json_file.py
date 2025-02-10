#!/usr/bin/python3
"""
This module provides the function 
"""
import json


def save_to_json_file(my_obj, filename):
    """
    This function save the representation on json of object
    in a file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
