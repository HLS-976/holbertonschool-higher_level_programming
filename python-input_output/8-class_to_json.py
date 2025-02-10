#!/usr/bin/python3
"""This module provides the function class_to_json"""
import json


def class_to_json(obj):
    """
    This function returns the dictionnary description
    of an object
    """
    return json.dumps(obj.__dict__)
