#!/usr/bin/python3
"""Defines a function that checks if an object is instance of a class."""


def is_same_class(obj, a_class):
    """returns whether obj is instance of a_class"""
    if type(obj) == a_class:
        return True
    return False
