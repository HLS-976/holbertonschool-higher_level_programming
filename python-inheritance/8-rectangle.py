#!/usr/bin/python3
"""Module for BaseGeometry class."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class represents a rectangle
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = height
        self.__height = height
