#!/usr/bin/python3
def print_square(size):

	if type(size) is int:
		if size >= 0:
			for a in range(size):
				for b in range(size):
					print("#", end="")
				print("")
		else:
			raise ValueError("size must be >= 0")
	else:
		raise TypeError("size must be an integer")
