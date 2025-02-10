#!/usr/bin/python3
"""This module provides the function load_from_json"""
import json


def load_from_json_file(filename):
    """
    this function deserialize an json string
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
