#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    final = " ".join(('{:d}'.format(a) for a in b) for b in matrix)
    print(final)
