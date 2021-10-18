#!/usr/bin/python3
"""Python3 Interpreter Location"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        text_1 = "[Square] ({}) ".format(self.id)
        text_2 = "{}/{} - ".format(self.x, self.y)
        text_3 = "{}".format(self.size)
        return text_1 + text_2 + text_3

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        size = self.size
