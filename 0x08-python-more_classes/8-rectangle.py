#!/usr/bin/python3
""" Class Rectangle """


class Rectangle:
    """ Empty class  """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ method is executed now """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ return  area """
        return (self.__height * self.__width)

    def perimeter(self):
        """ return  perimeter """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """ Prints string  """
        strrepr = ''
        if self.__height == 0 or self.__width == 0:
            return strrepr
        else:
            symbol = str(self.print_symbol)
            for i in range(0, self.__height):
                strrepr = strrepr + "{}".format(symbol*self.__width)
                if i != self.__height - 1:
                    strrepr = strrepr + '\n'
            return (strrepr)

    def __repr__(self):
        """ return object  """
        return("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """ delete an instance """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangle  """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
