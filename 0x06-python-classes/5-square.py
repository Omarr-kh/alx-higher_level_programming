#!/usr/bin/python3
"""Square model"""


class Square:
    """Defines square"""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: length of a square.
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, s):
        if not isinstance(s, int):
            raise TypeError("size must be an integer")
        if s < 0:
            raise ValueError("size must be >= 0")
        self.__size = s

    def area(self):
        return self.__size ** 2

    def my_print(self):
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="\n" if j == self.size - 1 and i != j else "")
        print()
