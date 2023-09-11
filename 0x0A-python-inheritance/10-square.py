#!/usr/bin/python3
"""Defines a square class that inherits from rectangle class"""
Rectangle = __import__('9-Rectangle').Rectangle


class Square(Rectangle):
    """represents square class"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
