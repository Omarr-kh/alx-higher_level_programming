#!/usr/bin/python3
"""Defines a class that inherits from class list."""


class MyList(list):
    """a Class that inherits from list class"""

    def print_sorted(self):
        """prints elements of list in sorted order (ascending)"""
        print(sorted(self))
