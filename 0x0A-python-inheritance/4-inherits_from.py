#!/usr/bin/python3
"""Defines a function that checks if an object is instance of a class."""


def is_kind_of_class(obj, a_class):
    """returns whether obj is instance of a_class"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
