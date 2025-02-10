#!/usr/bin/python3
"""
This module provides the function append_write
"""


def append_write(filename="", text=""):
    """
    This function append at end file a content given
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
