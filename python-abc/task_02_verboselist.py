#!/usr/bin/python3
"""This module provides classes"""


class VerboseList(list):
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        super().extend(item)
        print("Extended the list with [{}] items.".format(len(item)))

    def remove(self, item):
        super().remove(item)
        print("Removed [{}] from the list.".format(item))

    def pop(self, item=-1):
        value = super().pop(item)
        print("Popped [{}] from the list.".format(value))
