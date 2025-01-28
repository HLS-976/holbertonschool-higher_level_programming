#!/usr/bin/python3
"""
This module provides the square class
This is an empty class
"""


class Square:
    """
    The Square is an empty class
    """
    __size = None

    def __init__(self, size=0):
        """
        Creates an instance of square with size attribute
        Checks if size is an integer else raise an exception
        """
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        This method returns the area square result
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        this method get the value of __size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        this method set a value in __size
        """
        self.__size = value
