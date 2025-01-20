#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    length = len(my_list)
    new_list = [0] * length
    i = 0

    while (i < length):
        if (my_list[i] % 2 == 0):
            new_list[i] = True
        else:
            new_list[i] = False
        i = i + 1
    
    return new_list
