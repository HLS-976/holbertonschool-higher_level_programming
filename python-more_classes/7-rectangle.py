#!/usr/bin/python3
"""
This module provides the Rectangle class
This class represent a rectangle
"""


class Rectangle:
    """
    This class is a representation of a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if (self.__width == 0 or self.__height == 0):
            return ""
        rect = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rect += "{}".format(self.print_symbol)
            if (i != self.__height - 1):
                rect += "\n"
        return rect

    def __repr__(self):
        return (f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
