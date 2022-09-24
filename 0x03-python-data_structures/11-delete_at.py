#!/usr/bin/python3
def delete_at(listof=[], idx=0):
    length_list = len(listof) - 1
    if idx < 0 or idx > length_list:
        return(listof)
    else:
        del listof[idx]
        return(listof)
