#!/usr/bin/python3
"""Defines an class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represents rectangle class"""

    def __init__(self, width, height):
        """Initialize a rectangle"""
        self.integer_validator("width", width)
        self.width = width
        self.integer_validator("height", height)
        self.height = height

    def area(self):
        """returns area of rectangle"""
        return self.height * self.width
    
    def __str__(self):
        return f"[{self.__class__.__name__}] {self.width}/{self.height}"
