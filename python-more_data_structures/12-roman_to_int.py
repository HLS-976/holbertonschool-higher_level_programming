#!/usr/bin/python3

def roman_to_int(roman_string):
    convert_number = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
        }
    new_arr = []
    result = 0

    if (roman_string is None or type(roman_string) is not str):
        return (0)
    else:
        if ("IX" in roman_string):
            roman_string = roman_string.replace("IX", "")
            result += 9
        if ("XC" in roman_string):
            roman_string = roman_string.replace("XC", "")
            result += 90
        if ("CM" in roman_string):
            roman_string = roman_string.replace("CM", "")
            result += 900
        for i in roman_string:
            for j in convert_number:
                if (j == i):
                    result += convert_number[j]
    return result
