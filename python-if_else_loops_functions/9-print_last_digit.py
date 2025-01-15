#!/usr/bin/python3


def print_last_digit(number):
    print("{}".format(number % 10), end="")
    return number % 10


a = print_last_digit(242452)
print(f"{a}")