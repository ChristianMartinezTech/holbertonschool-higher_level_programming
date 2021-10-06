#!/usr/bin/python3

div = 3
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

new_matrix = []

for i in range(len(matrix)):
    new_matrix[i] = (matrix[i] / div)

print(new_matrix)
print(matrix)
