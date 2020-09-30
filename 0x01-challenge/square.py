#!/usr/bin/python3
""" My Square """


class square():
    """ Class Square """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def areaOfMySquare(self):
        """ Area of the square """
        return self.width * self.width

    def permiterOfMySquare(self):
        """ Perimeter """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Print """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.areaOfMySquare())
    print(s.permiterOfMySquare())
