#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_2 = [[a ** 2 for a in b] for b in matrix]
    return(matrix_2)
