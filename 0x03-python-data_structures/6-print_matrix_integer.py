#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for b in matrix:
        final = " ".join('{:d}'.format(a) for a in b)
        print(final)
