#!/usr/bin/python3
def complex_delete(a_dic, value):
    new_dic = list(a_dic.keys())
    {a_dic.pop(key) for key in new_dic if a_dic[key] == value}
    return (a_dic)
