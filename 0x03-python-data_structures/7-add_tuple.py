#!/usr/bin/python3
def add_tuple(tupA=(), tupB=()):
    if (len(tupA) == 0):
        tupA = (0, 0)
    elif (len(tupA) == 1):
        tupA = (tupA[0], 0)
    if (len(tupB) == 0):
        tupB = (0, 0)
    elif (len(tupB) == 1):
        tupB = (tupB[0], 0)

    return (tupA[0] + tupB[0], tupA[1] + tupB[1])
