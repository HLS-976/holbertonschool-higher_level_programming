#!/usr/bin/python3


def number_keys(a_dictionary):
    key_number = 0

    for element in a_dictionary:
        if (a_dictionary[element]):
            key_number += 1
    return key_number
