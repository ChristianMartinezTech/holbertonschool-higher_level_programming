#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res = tuple(map(lambda a, b: a + b, tuple_a, tuple_b))
    return(res)
