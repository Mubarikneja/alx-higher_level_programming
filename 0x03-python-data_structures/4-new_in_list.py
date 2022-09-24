#!/usr/bin/python3
def new_in_list(listof, idx, element):
    listlength = len(listof) - 1
    if (idx < 0 or idx > listlength):
        return (listof)
    else:
        new_list = listof[:]
        new_list[idx] = element
        return (new_list)
