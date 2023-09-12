#!/usr/bin/python3
"""Definition for a function that reads a text file"""


def read_file(filename=""):
    """reads a file"""
    with open(filename, encoding="utf-8") as f:
        print(list(f))
