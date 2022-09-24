#!/usr/bin/python3
def print_reversed_list_integer(listof=[]):
    if listof:
        listof.reverse()
        for number in listof:
            print("{:d}".format(number))
