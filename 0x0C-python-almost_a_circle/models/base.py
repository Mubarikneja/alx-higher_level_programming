#!/usr/bin/python3
""" Class Base will be the 'base' """


class Base:
    """ This class will be the 'base'  """

    __nb_objects = 0

    def __init__(self, id=None):
        """ init method """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
