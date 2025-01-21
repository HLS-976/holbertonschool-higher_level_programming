#!/usr/bin/python3

def roman_to_int(roman_string):
    convert_number = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = i = 0

    if (roman_string is None or type(roman_string) is not str):
        return (0)
    
    while (i < len(roman_string)):
        for j in convert_number:
            if (j == roman_string[i]):
                result += convert_number[j]
        i = i + 1
    return result
