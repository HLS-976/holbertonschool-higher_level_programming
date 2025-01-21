#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    new_dict = a_dictionary

    if key in a_dictionary:
        new_dict[key] = value
    else:
        new_dict[key] = value
    
    return new_dict
