#!/usr/bin/pyhton3
# 3-say_my_name.py
"""Functoin definition for say_my_name"""


def say_my_name(first_name, last_name=""):
    """ function prints a name

    Args:
        first_name: (str) first name
        last_name: (str) second name (optional)
    Raise:
        TypeError: if either of args are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
