#!/usr/bin/python3
def simple_delete(a_dic, key=""):
    if key in a_dic.keys():
        a_dic.pop(key)
    return(a_dic)
