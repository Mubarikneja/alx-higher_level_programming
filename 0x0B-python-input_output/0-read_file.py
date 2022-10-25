#!/usr/bin/python3
""" read a text file and prints  stdout """


def read_file(filename=""):
    """ read a text file (UTF8) and prints  stdout """
    with open(filename, encoding='utf8') as f:
        print(f.read(), end='')
