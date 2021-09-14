#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for b in matrix:
        print(" ".join('{:d}'.format(a) for a in b))
