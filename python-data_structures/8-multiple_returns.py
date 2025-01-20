#!/usr/bin/python3


def multiple_returns(sentence):
    first_char = ""
    length = len(sentence)
    first_char = None if (sentence == "") else sentence[0]
    new_tuple = (length, first_char)
    return (new_tuple)
