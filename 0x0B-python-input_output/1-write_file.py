#!/usr/bin/python3
"""
writes a string to a text then returns the number of
characters written
"""


def write_file(filename="", text=""):
    """
    writes a string to a text then and returns the number of
    characters written
    """
    with open(filename, 'w+', encoding='utf-8') as f:
        return(f.write(text))
