#!/usr/bin/python3
""" My Square """


class Square():
    """ Class Square """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def check_size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    @property
    def width(self):
        return self.__size

    @width.setter
    def width(self, value):
        self.check_size(value)
        self.__size = value

    @property
    def height(self):
        return self.__size

    @height.setter
    def height(self, value):
        self.check_size(value)
        self.__size = value

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Perimeter """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Print """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
