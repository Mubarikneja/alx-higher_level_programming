#!/usr/bin/python3
def max_integer(listof=[]):
    if listof == []:
        return(None)
    listof.sort()
    return(listof[-1])
