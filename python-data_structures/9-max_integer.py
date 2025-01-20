#!/usr/bin/python3


def max_integer(my_list=[]):
    max = None
    for i in my_list:
        if (max < i):
            max = i
    return (max)
