#!/usr/bin/python3
def matrix_divided(matrix, div):

	if type(matrix) == list:
		for x in matrix:
			if not isinstance(x, (int, float)):
				raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
	else:
		raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

	if isinstance(div, (int, float)):
		if div == 0:
			raise ZeroDivisionError("ZeroDivisionError")
	else:
		raise TypeError("div must be a number")

	new_matrix = []
	for y in matrix:
		new_matrix.append(y / div)

	return new_matrix
	return matrix
