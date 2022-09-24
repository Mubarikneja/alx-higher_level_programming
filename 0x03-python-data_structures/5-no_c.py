#!/usr/bin/python3
def no_c(my_string):
    list_char = list(my_string)
    for char in list_char:
        if char == 'c' or char == 'C':
            list_char.remove(char)
    return("".join(list_char))
