#!/usr/bin/python3
def multiple_returns(sentence):

    if not sentence:
        sentence[0] = None
    else:
        return(tuple((len(sentence), sentence[0])))
