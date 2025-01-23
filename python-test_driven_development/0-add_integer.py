#!/usr/bin/python3


def add_integer(a, b=98):
    """
        add_integer - adds two integers and returns the result

        Arguments:
        a -- An integer or float, which will be converted to an integer
        b -- An integer or float, which will be converted to an integer

        The function takes as arguments two integers or floats,
        converts both numbers to integer if they are floats
        and returns the result of the addition.
    """
    if not (isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    if not (isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return (a + b)
