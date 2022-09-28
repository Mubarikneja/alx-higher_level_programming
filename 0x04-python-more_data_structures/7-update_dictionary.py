#!/usr/bin/python3
def update_dictionary(a_dic, key, value):
    if key in a_dic.keys():
        a_dic[key] = value
    else:
        a_dic[key] = value
    return(a_dic)
