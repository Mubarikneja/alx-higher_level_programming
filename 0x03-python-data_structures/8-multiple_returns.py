#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        myTup = (0, None)
    else:
        myTup = (len(sentence), sentence[:1])
    return(myTup)
