#!/usr/bin/python3
"""
This module provides the Rectangle class
This class represent a rectangle
"""


class Rectangle:
    """
    This class is a representation of a rectangle
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width
        """
        return self.__width

    @property
    def height(self):
        """
        Retrives the height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Sets value on width
        """
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets value on width
        """
        if not (isinstance(value, int)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
