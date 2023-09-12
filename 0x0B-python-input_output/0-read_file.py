#!/usr/bin/python3
"""Definition for a function that reads a text file"""


def read_file(filename=""):
    with open(filename) as f:
        print(list(f))
