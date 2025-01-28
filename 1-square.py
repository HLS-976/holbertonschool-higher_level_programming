#!/usr/bin/python3
"""
This module provides the square class
that define a square
"""


class Square:
    """
    The Square is a class that defines a square

    size -- private instance attribute
    """
    __size = None

    def __init__(self, size):
        """
        self: Self@Square,
        size: Any
        """
        self.__size = size
