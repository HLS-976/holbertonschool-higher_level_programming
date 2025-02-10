#!/usr/bin/python3
"""
This module provides the funciont write_file
"""


def write_file(filename="my_first_file.txt", text=""):
    """ Function that write in a file """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
