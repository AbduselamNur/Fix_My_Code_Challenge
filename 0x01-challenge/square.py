#!/usr/bin/python3
""" Module For Square Class """


class square():
    """
    square class that has Area and Premiter
    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Constructor function"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """Return The Perimeter of The Squre"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Return The width and height"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Create Square Obj"""
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
