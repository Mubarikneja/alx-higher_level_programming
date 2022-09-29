#!/usr/bin/python3
def print_last_digit(num):
    if num < 0:
        num = num * -1
    lastdigit = num % 10
    print("{:d}".format(lastdigit), end="")
    return(lastdigit)
