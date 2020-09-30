#!/usr/bin/python3
""" My Square """


class square():
    """ Class Square """
    size = 0

    def __init__(self, *args, **kwargs):
        if kwargs:
            self.size = kwargs["width"]

    def area_of_my_square(self):
        """ Area of the square """
        return self.size * self.size

    def PermiterOfMySquare(self):
        """ Perimeter """
        return (self.size * 2) + (self.size * 2)

    def __str__(self):
        """ Print """
        return "{}/{}".format(self.size, self.size)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
