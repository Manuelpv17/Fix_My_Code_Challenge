#!/usr/bin/python3
""" My Square """


class Square():
    """ Class Square """

    width = 0
    height = 0

    def __init__(self, width, height):
        """ Init """
        self.width = width
        self.height = height

    def check_size(self, value):
        """ Check"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value <= 0:
            raise ValueError("size must be >= 0")

    @property
    def width(self):
        """ width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ width """
        self.check_size(value)
        self.__width = value

    @property
    def height(self):
        """ height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ height"""
        self.check_size(value)
        self.__height = value

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiterOfMySquare(self):
        """ Perimeter """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Print """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.permiterOfMySquare())
