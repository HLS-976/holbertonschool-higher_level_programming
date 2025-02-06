#!/usr/bin/python3
"""
This module provides the abstract package
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    This abstract class represent animal concept
    providing the abstract method sound
    """
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    This class represent a dog
    """
    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    This class represent a cat
    """
    def sound(self):
        return "Meow"
