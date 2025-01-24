#!/usr/bin/python3
"""
This module provides the print_square function
This function prints square formed by '#' character with a size
"""


def print_square(size):
    """
    print_square - Prints a square with a size formed by '#' character

    size -- The size of square

    This function checks if the size is an integer else throws an exception
    if size less than 0, the function throws an exception,
    if size is a float and is less than 0 the function throws an exception
    """
    if not (isinstance(size, int)):
        raise TypeError("size must be an integer")
    if (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print('#', end="")
        print('#')
