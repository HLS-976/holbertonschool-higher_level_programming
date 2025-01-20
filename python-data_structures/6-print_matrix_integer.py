#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if (matrix == [[]]):
        print()
    else:
        for i in matrix:
            for j in i:
                if (i[-1] != j):
                    print("{:d}".format(j), end=" ")
                else:
                    print("{:d}".format(j))
