#!/usr/bin/python3
"""Class definition for Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Representation of a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of Rectangle
        Args:
            width: (int) width of rectangle
            height: (int) height of rectangle
            x: (int) x coordinate of rectangle
            y: (int) y coordinate of rectangle
            id: (int) id of Rectangle
        Raises:
            TypeError: If width or height is not an int.
            ValueError: If width or height <= 0.
            TypeError: If x or y is not an int.
            ValueError: If x or y < 0.
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """getter method for the width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the Rectangle."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """set the y coordinate of the Rectangle"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """displays the Rectangle with the '#' character"""
        if self.__width == 0 or self.__height == 0:
            print("")
            return

        [print("") for i in range(self.__y)]
        for _ in range(self.__height):
            [print("", end="") for k in range(self.__x)]
            [print("#", end="") for j in range(self.__width)]

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args: (ints) New attribute values.
                - 1st argument for id attribute
                - 2nd argument for width attribute
                - 3rd argument for height attribute
                - 4th argument for x attribute
                - 5th argument for y attribute
            **kwargs: (dict) key/value pairs of attributes.
        """
        if args and len(args) != 0:
            counter = 0
            for arg in args:
                if counter == 0:
                    if arg is None:
                        self.__init__(self.__width,
                                      self.__height, self.__x, self.__y)
                    else:
                        self.id = arg
                elif counter == 1:
                    self.__width = arg
                elif counter == 2:
                    self.__height = arg
                elif counter == 3:
                    self.__x = arg
                elif counter == 4:
                    self.__y = arg
                counter += 1

        elif kwargs and len(kwargs) != 0:
            for k, val in kwargs.items():
                if k == "id":
                    if val is None:
                        self.__init__(self.__width,
                                      self.__height, self.__x, self.__y)
                    else:
                        self.__id = val
                elif k == "width":
                    self.__width = val
                elif k == "height":
                    self.__height = val
                elif k == "x":
                    self.__x = val
                elif k == "y":
                    self.__y = val

    def __str__(self):
        """Return the print() and str() representation of Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def to_dictionary(self):
        """returns dict representation of the class"""
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }
