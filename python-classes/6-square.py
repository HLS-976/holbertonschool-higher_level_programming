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
    __position = None

    def __init__(self, size=0, position=(0, 0)):
        """
        Creates an instance of square with size attribute
        Checks if size is an integer else raise an exception
        """
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not (isinstance(position, tuple)):
            raise TypeError("position must be a tuple of 2 positive")
        for item in position:
            if not isinstance(item, int) and item < 0:
                raise TypeError("position must be a tuple of 2 positive")

        self.__size = size
        self.__position = position

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
        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        This method returns the area square result
        """
        return self.__size ** 2

    def my_print(self):
        """
        This method prints the visually area formed by '#' charater
        """
        if self.__size == 0:
            print()
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            print("")
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    @property
    def position(self):
        """
        this method get the value on position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        This method set a value to position
        """
        if not (isinstance(value, tuple)):
            raise TypeError("position must be a tuple of 2 positive")
        for item in value:
            if not isinstance(item, int) and item < 0:
                raise TypeError("position must be a tuple of 2 positive")
        self.__position = value
