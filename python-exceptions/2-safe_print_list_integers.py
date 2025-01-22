#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    count =  0
    length = 0
    index = 0

    for i in my_list:
        length += 1
    try:
        if (x <= length):
            for i in range(0, x):
                if (type(my_list[i]) == int and my_list[i]):
                    print("{}".format(my_list[i]), end="")
                    count += 1
            print()
    except IndexError:
        pass
    return count
