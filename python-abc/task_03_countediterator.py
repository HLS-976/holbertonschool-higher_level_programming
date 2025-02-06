#!/usr/bin/python3
"""
This module provide a class
"""


class CountedIterator:
    def __init__(self, data):
        """Initialize the iterator and the counter"""
        self.iterator = iter(data)
        self.counter_track = 0

    def get_count(self):
        """Return the number of items"""
        return self.counter_track

    def __iter__(self):
        """Return the iterator itself"""
        return self

    def __next__(self):
        try:
            value = next(self.iterator)
            self.counter_track += 1
            return value
        except StopIteration:
            raise StopIteration
