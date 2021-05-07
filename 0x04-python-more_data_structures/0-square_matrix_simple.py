#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_2 = list(matrix)
    for row in range(len(matrix_2)):
        for col in range(len(matrix_2)):
            return((matrix_2[row][col]) ** 2)
