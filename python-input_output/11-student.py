#!/usr/bin/python3
"""
This module provides a class
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        This function return the attribute
        contained in a list
        """
        if attrs is None:
            return self.__dict__
        resultat = {}
        for attr in sorted(attrs):
            if attr in self.__dict__:
                resultat[attr] = self.__dict__[attr]
        return resultat

    def reload_from_json(self, json):
        """
        This function reloads the attributes from json
        """
        for key in json:
            if json[key] == self.__dict__[key]:
                self.__dict__[key] = json[key]
