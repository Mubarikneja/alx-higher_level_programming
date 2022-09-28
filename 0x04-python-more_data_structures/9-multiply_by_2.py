#!/usr/bin/python3
def multiply_by_2(a_dic):
    new_dic = a_dic.copy()
    for key in new_dic:
        new_dic[key] *= 2
    return(new_dic)
