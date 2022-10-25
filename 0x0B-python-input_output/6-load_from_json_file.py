#!/usr/bin/python3
""" creates an Object from JSON  """
import json


def load_from_json_file(filename):
    """ creates an Object from JSON  """
    with open(filename, 'r', encoding='utf8') as f:
        obj = json.load(f)
        return obj
