#!/usr/bin/python3


def uniq_add(my_list=[]):
    unique = []
    sum = 0
    for number in my_list:
        if number not in unique:
            unique.append(number)
            sum += number
    return sum
