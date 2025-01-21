#!/usr/bin/python3

def roman_to_int(roman_string):
    convert_number = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
    integer_value = 0
    prev_value = 0

    if (roman_string is None or type(roman_string) is not str):
        return (0)
    for char in reversed(roman_string):
        value = convert_number.get(char, 0)
        if value < prev_value:
            integer_value -= value
        else:
            integer_value += value
            prev_value = value
    return integer_value
