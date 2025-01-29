#!/usr/bin/python3
"""
This module provides the Rectangle class
This class represent a rectangle
"""


class Rectangle:
    """
    This class is a representation of a rectangle
    """
    __width = None
    __height = None

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

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

    def area(self):
        """
        Returns the area of a rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Returns the perimeter of a rectangle
        """
        if (self.__width == 0 or self.__height == 0):
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if (self.__height == 0 or self.height == 0):
            return ""
        rectangle = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle += "#"
            if (i != self.__height - 1):
                rectangle += "\n"
        return rectangle
    
    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"