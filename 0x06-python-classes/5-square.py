#!/usr/bin/python3
""" Class Square """


class Square:
    """ Class """
    def __init__(self, size=0):
        """ Constructor """
        self.size = size

    @property
    def size(self):
        """ Getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Calculated square area """
        return(self.__size * self.__size)

    def my_print(self):
        """ Print square """
        if self.size != 0:
            for square in range(0, self.size):
                print("#" * self.size)
        else:
            print("")
