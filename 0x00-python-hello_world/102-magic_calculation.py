#!/usr/bin/python3
import dis
def magic_calculation(a, b):
    a ** b
    a + b
dis.dis(magic_calculation(a, b))
