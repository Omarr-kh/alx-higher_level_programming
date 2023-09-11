#!/usr/bin/python3
"""Defines a function"""


def add_attribute(obj, attrib, val):
    """adds attribute to an object if possible"""
    if hasattr(obj, __dict__):
        setattr(obj, attrib, val)
    else:
        raise TypeError("can't add new attribute")
