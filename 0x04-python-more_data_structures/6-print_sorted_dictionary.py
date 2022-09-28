#!/usr/bin/python3
def print_sorted_dictionary(a_dic):
    for key in sorted(a_dic.keys()):
        print("{}:".format(key), a_dic[key])
