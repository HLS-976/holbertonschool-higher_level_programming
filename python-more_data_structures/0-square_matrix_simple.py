#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix
    for i in matrix:
        new_matrix = i
        for j in i:
            j = j ** 2
    return new_matrix



matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)

for i in matrix:
    print(f"{i}")

print()

for i in new_matrix:
    print(f"{i}")