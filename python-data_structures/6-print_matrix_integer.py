#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            if (i[-1] != j):
                print("{}".format(j), end=" ")
            else:
                print("{}".format(j))