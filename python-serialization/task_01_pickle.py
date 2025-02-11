#!/usr/bin/python3
"""
This module provides a class
"""
import pickle
from os import path


class CustomObject:
    """
    This is a custom class
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        prt = "Name: {}\nAge: {}\nIs Student: {}"
        print(prt.format(self.name, self.age, self.is_student))

    def serialize(self, filename):
        """
        This method serializes the curent object and save it
        to the filename
        """
        with open(filename, 'wb') as f:
            serialized = pickle.dumps(self)
            f.write(serialized)

    @classmethod
    def deserialize(cls, filename):

        with open(filename, 'rb') as f:
            deserialized = pickle.load(f)
            return deserialized
