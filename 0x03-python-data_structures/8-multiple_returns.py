#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0]

    if not sentence:
        return length, None
    else:
        return (length, first)
