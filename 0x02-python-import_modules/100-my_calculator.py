#!/usr/bin/python3
if __name__ == '__main__':
	import sys
	from calculator_1 import add, sub, mul, div

	f_num = sys.argv[0]
	l_num = sys.argv[2]

	if len(sys.argv) == 3:
		if sys.argv[1] == '+':
			print("{} + {} = {}".format(f_num, l_num, f_num + l_num))
		elif sys.argv[1] == '-':
			print("{} - {} = {}".format(f_num, l_num, f_num - l_num))
		elif sys.argv[1] == '*':
			print("{} * {} = {}".format(f_num, l_num, f_num * l_num))
		elif sys.argv[1] == '/':
			print("{} / {} = {}".format(f_num, l_num, f_num / l_num))
		else:
			print("Unknown operator. Available operators: +, -, * and /")
			exit(1)
	else:
		print("Usage: ./100-my_calculator.py <a> <operator> <b>")
		exit(1)
