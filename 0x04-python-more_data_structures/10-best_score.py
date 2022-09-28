#!/usr/bin/python3
def best_score(a_dic):
    if a_dic:
        max_value = max(a_dic, key=a_dic.get)
    else:
        max_value = None
    return(max_value)
