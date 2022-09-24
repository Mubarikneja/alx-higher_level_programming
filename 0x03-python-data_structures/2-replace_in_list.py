#!/usr/bin/python3
def replace_in_list(listof, idx, elem):
    listlength = len(listof) - 1
    if (idx < 0 or idx > listlength):
        return (listof)
    else:
        listof[idx] = elem
        return (listof)
