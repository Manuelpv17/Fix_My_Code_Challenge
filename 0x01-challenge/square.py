#!/usr/bin/python3
""" My Square """


class Square():
    """ Class Square """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        for value in kwargs.values():
            self.width = value
            self.height = value

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

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
