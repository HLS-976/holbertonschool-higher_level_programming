#!/usr/bin/python3
"""
This module provides two function
"""
from os import path
import json


def serialize_and_save_to_file(data, filename):
    """
    This function serialize and save data to the specified file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        serialized = json.dumps(data)
        f.write(serialized)


def load_and_deserialize(filename):
    """
    This function deserialize the content from the filename
    """
    with open(filename, 'r') as f:
        return json.loads(f.read())
