#!/usr/bin/python3
""" Class Rectangle """


class Rectangle:
    """ Empty class Rectangle that defines a rectangle """
    def __init__(self, width=0, height=0):
        """ method is executed now """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ Geter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Seter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Geter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Seter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
