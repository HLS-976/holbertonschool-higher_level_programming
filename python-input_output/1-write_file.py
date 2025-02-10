#!/usr/bin/python3
"""
This module provides the funciont write_file
"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
