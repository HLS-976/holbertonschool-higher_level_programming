#!/usr/bin/python3
"""
This module provides the class Mylist
"""


class MyList(list):
    """
    this class prints the list by sorting an ascending
    """
    def print_sorted(self):
        self.sort()
