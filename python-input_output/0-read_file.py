#!/usr/bin/python3
"""
This module provides the function read_file
"""


def read_file(filename=""):
    """
    This function print the content of a file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
