#!/usr/bin/python3


def best_score(a_dictionary):
    big = 0
    element = None

    if (a_dictionary is None):
        return element

    for key, value in a_dictionary.items():
        if (value > big):
            big = value
            element = key
    return element
