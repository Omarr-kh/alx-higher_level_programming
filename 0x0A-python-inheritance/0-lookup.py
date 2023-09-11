#!/usr/bin/python3
"""Defines a function that returns object attributes."""


def lookup(obj):
    """return a list of available attributes for the obj"""
    return (dir(obj))
