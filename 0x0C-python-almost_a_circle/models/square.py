#!/usr/bin/python3
"""Class definition for Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Representation of a Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of Square
        Args:
            size: (int) size of Square
            x: (int) x coordinate of Square
            y: (int) y coordinate of Square
            id: (int) id of Square
        Raises:
            TypeError: If size is not an int.
            ValueError: If size <= 0.
            TypeError: If x or y is not an int.
            ValueError: If x or y < 0.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for the size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for the size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square.

        Args:
            *args (ints): New attribute values.
                - 1st id attribute
                - 2nd size attribute
                - 3rd x attribute
                - 4th y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            counter = 0
            for arg in args:
                if counter == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif counter == 1:
                    self.size = arg
                elif counter == 2:
                    self.x = arg
                elif counter == 3:
                    self.y = arg
                counter += 1

        elif kwargs and len(kwargs) != 0:
            for k, val in kwargs.items():
                if k == "id":
                    if val is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = val
                elif k == "size":
                    self.size = val
                elif k == "x":
                    self.x = val
                elif k == "y":
                    self.y = val

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
