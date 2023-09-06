#!/usr/bin/python3
# 4-print_square.py
"""Definition of a square-printing function."""


def print_square(size):
    """Print a square with the # character.

    Args:
        size: The height/width of the square(int).
    Raises:
        TypeError: size is not an integer.
        ValueError: size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        for i in range(size):
            print("#", end="")
        print("")
