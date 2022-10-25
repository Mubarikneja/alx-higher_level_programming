#!/usr/bin/python3
"""
returns the dictionary description 
(list, dictionary, string, integer and boolean)
for JSON serialization 
"""


def class_to_json(obj):
    """
    returns the dictionary description 
    (list, dictionary, string, integer and boolean)
    for JSON serialization 
    """
    return obj.__dict__
