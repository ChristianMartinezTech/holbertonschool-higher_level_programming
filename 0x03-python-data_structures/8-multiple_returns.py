#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)

    if not sentence:
        sentence[0] = None
    else:
        return(tuple((length, sentence[0])))
