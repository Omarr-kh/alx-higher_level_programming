#!/usr/bin/python3
"""Defines a function that writes Object to txt file in JSON."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to file using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
