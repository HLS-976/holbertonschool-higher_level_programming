#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sort_dict = sorted(a_dictionary.items())

    for element in sort_dict:
        print("{}: {}".format(element[0], element[1]))
