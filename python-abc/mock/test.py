#!/usr/bin/python3


class Rectangle:

    number_of_instance = 0

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        number_of_instance += 1


    @property
    def width(self):
        return self.__width
    
     @property
    def height(self):
        return self.__height
    
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value
    
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value
